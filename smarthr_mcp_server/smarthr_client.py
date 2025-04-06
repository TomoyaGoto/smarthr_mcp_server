import os
import requests
from typing import Dict, Any, Optional, List, Union
from pydantic import BaseModel, Field, validator
from enum import Enum
from datetime import datetime

class Address(BaseModel):
    """
    住所リクエストのモデル
    """
    country_number: Optional[str] = None
    zip_code: Optional[str] = None
    pref: Optional[str] = None
    city: Optional[str] = None
    street: Optional[str] = None
    building: Optional[str] = None
    literal_yomi: Optional[str] = None

class AttachmentParams(BaseModel):
    file_name: str
    content: str

class LiveTogetherType(str, Enum):
    """
    同居別居リクエストのモデル
    """
    living_together = "living_together"
    living_separately = "living_separately"

class DepartmentCreateRequest(BaseModel):
    """
    部署作成リクエストのモデル
    """
    name: str
    position: Optional[int] = None
    code: Optional[str] = None
    parent_id: Optional[str] = None

    @validator('name')
    def validate_name(cls, v):
        """
        部署名に/を含めないようにバリデーション
        """
        if '/' in v:
            raise ValueError("部署名に'/'を含めることはできません")
        return v

class JobTitleCreateRequest(BaseModel):
    """
    役職作成リクエストのモデル
    """
    name: str
    rank: int
    code: Optional[str] = None

    @validator('rank')
    def validate_rank(cls, v):
        """
        役職のランクが1〜99999の範囲であることをバリデーション
        """
        if v < 1 or v > 99999:
            raise ValueError("役職のランクは1〜99999の範囲で指定してください")
        return v

class JobTitleUpdateRequest(BaseModel):
    """
    役職更新リクエストのモデル
    """
    name: str
    rank: int

    @validator('rank')
    def validate_rank(cls, v):
        """
        役職のランクが1〜99999の範囲であることをバリデーション
        """
        if v < 1 or v > 99999:
            raise ValueError("役職のランクは1〜99999の範囲で指定してください")
        return v

class JobTitlePartialUpdateRequest(BaseModel):
    """
    役職部分更新リクエストのモデル
    """
    name: Optional[str] = None
    rank: Optional[int] = None
    code: Optional[str] = None

    @validator('rank')
    def validate_rank(cls, v):
        """
        役職のランクが1〜99999の範囲であることをバリデーション
        """
        if v is not None and (v < 1 or v > 99999):
            raise ValueError("役職のランクは1〜99999の範囲で指定してください")
        return v

class EmploymentTypeCreateRequest(BaseModel):
    """
    雇用形態作成リクエストのモデル
    """
    name: str
    code: Optional[str] = None

class EmploymentTypeUpdateRequest(BaseModel):
    """
    雇用形態更新リクエストのモデル
    """
    name: str

class EmploymentTypePartialUpdateRequest(BaseModel):
    """
    雇用形態部分更新リクエストのモデル
    """
    name: Optional[str] = None
    code: Optional[str] = None

class DepartmentDiscontinueRequest(BaseModel):
    """
    部署廃止リクエストのモデル
    """
    discontinued_date: str

    @validator('discontinued_date')
    def validate_discontinued_date(cls, v):
        """
        廃止日のバリデーション
        """
        try:
            discontinued_date = datetime.strptime(v, '%Y-%m-%d').date()
            if discontinued_date > datetime.now().date():
                raise ValueError("廃止日は過去の日付のみ指定できます")
        except ValueError:
            raise ValueError("廃止日は YYYY-MM-DD 形式で指定してください")
        return v

class DepartmentPartialUpdateRequest(BaseModel):
    """
    部署部分更新リクエストのモデル
    """
    name: Optional[str] = None
    position: Optional[int] = None
    code: Optional[str] = None
    parent_id: Optional[str] = None

    @validator('name')
    def validate_name(cls, v):
        """
        部署名に/を含めないようにバリデーション
        """
        if v is not None and '/' in v:
            raise ValueError("部署名に'/'を含めることはできません")
        return v

class DepartmentUpdateRequest(BaseModel):
    """
    部署更新リクエストのモデル
    """
    name: str
    position: Optional[int] = None
    code: Optional[str] = None
    parent_id: Optional[str] = None

    @validator('name')
    def validate_name(cls, v):
        """
        部署名に/を含めないようにバリデーション
        """
        if '/' in v:
            raise ValueError("部署名に'/'を含めることはできません")
        return v

class GradeCreateRequest(BaseModel):
    """
    等級作成リクエストのモデル
    """
    name: str
    rank: int

    @validator('rank')
    def validate_rank(cls, v):
        """
        等級のランクが1〜99999の範囲であることをバリデーション
        """
        if v < 1 or v > 99999:
            raise ValueError("等級のランクは1〜99999の範囲で指定してください")
        return v

class GradeUpdateRequest(BaseModel):
    """
    等級更新リクエストのモデル
    """
    name: str
    rank: int

    @validator('rank')
    def validate_rank(cls, v):
        """
        等級のランクが1〜99999の範囲であることをバリデーション
        """
        if v < 1 or v > 99999:
            raise ValueError("等級のランクは1〜99999の範囲で指定してください")
        return v

class GradePartialUpdateRequest(BaseModel):
    """
    等級部分更新リクエストのモデル
    """
    name: Optional[str] = None
    rank: Optional[int] = None

    @validator('rank')
    def validate_rank(cls, v):
        """
        等級のランクが1〜99999の範囲であることをバリデーション
        """
        if v is not None and (v < 1 or v > 99999):
            raise ValueError("等級のランクは1〜99999の範囲で指定してください")
        return v

class JobCategoryCreateRequest(BaseModel):
    """
    職種作成リクエストのモデル
    """
    name: str

class JobCategoryUpdateRequest(BaseModel):
    """
    職種更新リクエストのモデル
    """
    name: str

class JobCategoryPartialUpdateRequest(BaseModel):
    """
    職種部分更新リクエストのモデル
    """
    name: Optional[str] = None

class DependentCreateRequest(BaseModel):
    """
    家族情報作成リクエストのモデル
    """
    relation_id: str
    is_spouse: Optional[bool] = None
    last_name: str
    first_name: str
    last_name_yomi: Optional[str] = None
    first_name_yomi: Optional[str] = None
    birth_at: str
    moved_at: Optional[str] = None
    gender: str
    job: Optional[str] = None
    basic_pension_number: Optional[str] = None
    basic_pension_number_image: Optional[AttachmentParams] = None
    live_together_type: LiveTogetherType
    address: Optional[Address] = None
    tel_number: Optional[str] = None
    handicapped_type: Optional[str] = None
    handicapped_note_type: Optional[str] = None
    handicapped_note_delivery_at: Optional[str] = None
    handicapped_image: Optional[AttachmentParams] = None
    remittance_to_relative: Optional[bool] = None
    remittance_image1: Optional[AttachmentParams] = None
    remittance_image2: Optional[AttachmentParams] = None
    remittance_image3: Optional[AttachmentParams] = None
    international_student: Optional[bool] = None
    international_student_image: Optional[AttachmentParams] = None
    social_insurance_support_type: Optional[str] = "supported"
    income: Optional[int] = None
    monthly_income: Optional[int] = None
    soc_ins_qualified_at: Optional[str] = None
    soc_ins_qualified_reason: Optional[str] = None
    soc_ins_disqualified_at: Optional[str] = None
    disqualified_reason_type: Optional[str] = None
    disqualified_reason: Optional[str] = None
    tax_law_support_type: Optional[str] = "supported"
    tax_deduction_income: Optional[int] = None
    tax_deduction_qualified_at: Optional[str] = None
    tax_deduction_qualified_reason: Optional[str] = None
    tax_deduction_disqualified_at: Optional[str] = None
    tax_deduction_disqualified_reason_type: Optional[str] = None
    tax_deduction_disqualified_reason: Optional[str] = None
    maternity_handbook_image: Optional[AttachmentParams] = None
    kinship_image: Optional[AttachmentParams] = None
    code: Optional[str] = None

    @validator('gender')
    def validate_gender(cls, v):
        if v not in ['male', 'female']:
            raise ValueError("性別（gender）は 'male' または 'female' を指定してください")
        return v

class DependentUpdateRequest(DependentCreateRequest):
    """
    家族情報更新リクエストのモデル
    """
    pass

class DependentPartialUpdateRequest(BaseModel):
    """
    家族情報部分更新リクエストのモデル
    """
    relation_id: str
    is_spouse: Optional[bool] = None
    last_name: str
    first_name: str
    last_name_yomi: Optional[str] = None
    first_name_yomi: Optional[str] = None
    birth_at: str
    moved_at: Optional[str] = None
    gender: str
    job: Optional[str] = None
    basic_pension_number: Optional[str] = None
    basic_pension_number_image: Optional[AttachmentParams] = None
    live_together_type: LiveTogetherType
    address: Optional[Address] = None
    tel_number: Optional[str] = None
    handicapped_type: Optional[str] = None
    handicapped_note_type: Optional[str] = None
    handicapped_note_delivery_at: Optional[str] = None
    handicapped_image: Optional[AttachmentParams] = None
    remittance_to_relative: Optional[bool] = None
    remittance_image1: Optional[AttachmentParams] = None
    remittance_image2: Optional[AttachmentParams] = None
    remittance_image3: Optional[AttachmentParams] = None
    international_student: Optional[bool] = None
    international_student_image: Optional[AttachmentParams] = None
    social_insurance_support_type: Optional[str] = None
    income: Optional[int] = None
    monthly_income: Optional[int] = None
    soc_ins_qualified_at: Optional[str] = None
    soc_ins_qualified_reason: Optional[str] = None
    soc_ins_disqualified_at: Optional[str] = None
    disqualified_reason_type: Optional[str] = None
    disqualified_reason: Optional[str] = None
    tax_law_support_type: Optional[str] = None
    tax_deduction_income: Optional[int] = None
    tax_deduction_qualified_at: Optional[str] = None
    tax_deduction_qualified_reason: Optional[str] = None
    tax_deduction_disqualified_at: Optional[str] = None
    tax_deduction_disqualified_reason_type: Optional[str] = None
    tax_deduction_disqualified_reason: Optional[str] = None
    maternity_handbook_image: Optional[AttachmentParams] = None
    kinship_image: Optional[AttachmentParams] = None
    code: Optional[str] = None

    def has_required_patch_fields(self) -> bool:
        required = [
            self.last_name, self.first_name, self.birth_at,
            self.gender, self.live_together_type, self.relation_id
        ]
        return all(required)

# 性別
class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"

class EmploymentStatus(str, Enum):
    EMPLOYED = "employed"
    ABSENT = "absent"
    RETIRED = "retired"

class EmploymentType(str, Enum):
    BOARD_MEMBER = "board_member"
    FULL_TIMER = "full_timer"
    CONTRACT_WORKER = "contract_worker"
    PERMATEMP = "permatemp"
    PART_TIMER = "part_timer"
    OUTSOURCING_CONTRACTOR = "outsourcing_contractor"
    ETC = "etc"

# カスタムフィールド
class CustomField(BaseModel):
    template_id: str
    value: Union[str, int, float, None]
    file_name: Optional[str] = None

# 住所情報
class Address(BaseModel):
    country_number: Optional[str] = None
    zip_code: Optional[str] = None
    pref: Optional[str] = None
    city: Optional[str] = None
    street: Optional[str] = None
    building: Optional[str] = None
    literal_yomi: Optional[str] = None

# 添付ファイルパラメータ
class AttachmentParams(BaseModel):
    file_name: Optional[str] = None
    content: Optional[str] = None  # Base64エンコード済み文字列

# 口座情報
class BankAccount(BaseModel):
    bank_code: str
    bank_branch_code: str
    account_type: str
    account_number: str
    account_holder_name: str
    bankbook_image: Optional[AttachmentParams] = None
    bank_account_setting_id: Optional[str] = None

# CrewCreateRequest
class CrewCreateRequest(BaseModel):
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    last_name_yomi: Optional[str] = None
    first_name_yomi: Optional[str] = None
    email: Optional[str] = None
    gender: Optional[Gender] = None
    birth_at: Optional[str] = None  # YYYY-MM-DD format
    employment_type_id: Optional[str] = None
    emp_type: Optional[EmploymentType] = None
    department_ids: Optional[List[str]] = None
    department: Optional[str] = None
    positions: Optional[List[str]] = None
    position: Optional[str] = None
    emp_status: Optional[EmploymentStatus] = None
    entered_at: Optional[str] = None  # YYYY-MM-DD format
    resigned_at: Optional[str] = None  # YYYY-MM-DD format
    custom_fields: Optional[List[CustomField]] = None

    user_id: Optional[str] = None
    biz_establishment_id: Optional[str] = None
    emp_code: Optional[str] = None

    business_last_name: Optional[str] = None
    business_first_name: Optional[str] = None
    business_last_name_yomi: Optional[str] = None
    business_first_name_yomi: Optional[str] = None

    tel_number: Optional[str] = None
    address: Optional[Address] = None
    address_head_of_family: Optional[str] = None
    address_relation_name: Optional[str] = None

    emergency_relation_name: Optional[str] = None
    emergency_last_name: Optional[str] = None
    emergency_first_name: Optional[str] = None
    emergency_last_name_yomi: Optional[str] = None
    emergency_first_name_yomi: Optional[str] = None
    emergency_tel_number: Optional[str] = None
    emergency_address: Optional[Address] = None

    resident_card_address: Optional[Address] = None
    resident_card_address_head_of_family: Optional[str] = None
    resident_card_address_relation_name: Optional[str] = None

    grade: Optional[str] = None
    job_category: Optional[str] = None
    occupation: Optional[str] = None
    resigned_reason: Optional[str] = None

    emp_ins_insured_person_number: Optional[str] = None
    emp_ins_insured_person_number_unknown_reason_type: Optional[str] = None
    emp_ins_qualified_at: Optional[str] = None
    emp_ins_disqualified_at: Optional[str] = None

    previous_workplace: Optional[str] = None
    previous_employment_start_on: Optional[str] = None
    previous_employment_end_on: Optional[str] = None

    soc_ins_insured_person_number: Optional[int] = None
    hel_ins_insured_person_number: Optional[int] = None
    basic_pension_number: Optional[str] = None
    first_enrolling_in_emp_pns_ins_flag: Optional[bool] = None
    basic_pension_number_unknown_reason_type: Optional[str] = None

    first_workplace: Optional[str] = None
    first_workplace_address_text: Optional[str] = None
    first_employment_start_on: Optional[str] = None
    first_employment_end_on: Optional[str] = None

    last_workplace: Optional[str] = None
    last_workplace_address_text: Optional[str] = None
    last_employment_start_on: Optional[str] = None
    last_employment_end_on: Optional[str] = None

    soc_ins_qualified_at: Optional[str] = None
    soc_ins_disqualified_at: Optional[str] = None

    having_spouse: Optional[bool] = None
    spouse_yearly_income: Optional[int] = None

    monthly_income_currency: Optional[int] = None
    monthly_income_goods: Optional[int] = None
    monthly_standard_income_updated_at: Optional[str] = None
    monthly_standard_income_hel: Optional[int] = None
    monthly_standard_income_pns: Optional[int] = None

    nearest_station_and_line: Optional[str] = None
    commutation_1_expenses: Optional[int] = None
    commutation_1_period: Optional[str] = None
    commutation_1_single_fare: Optional[int] = None
    commutation_2_expenses: Optional[int] = None
    commutation_2_period: Optional[str] = None
    commutation_2_single_fare: Optional[int] = None

    foreign_resident_last_name: Optional[str] = None
    foreign_resident_first_name: Optional[str] = None
    foreign_resident_middle_name: Optional[str] = None
    foreign_resident_card_number: Optional[str] = None
    nationality_code: Optional[str] = None
    resident_status_type: Optional[str] = None
    resident_status_other_reason: Optional[str] = None
    resident_end_at: Optional[str] = None
    having_ex_activity_permission: Optional[str] = None
    other_be_workable_type: Optional[str] = None
    contract_type: Optional[str] = None
    contract_start_on: Optional[str] = None
    contract_end_on: Optional[str] = None
    contract_renewal_type: Optional[str] = None
    tax_cd: Optional[str] = None
    handicapped_type: Optional[str] = None
    handicapped_note_type: Optional[str] = None
    handicapped_note_delivery_at: Optional[str] = None

    working_student_flag: Optional[bool] = None
    school_name: Optional[str] = None
    enrolled_at: Optional[str] = None
    working_student_income: Optional[int] = None

    employment_income_flag: Optional[bool] = None
    business_income_flag: Optional[bool] = None
    devidend_income_flag: Optional[bool] = None
    estate_income_flag: Optional[bool] = None

    widow_type: Optional[str] = None
    widow_reason_type: Optional[str] = None
    widow_memo: Optional[str] = None

    payment_period_id: Optional[str] = None

    profile_image: Optional[AttachmentParams] = None
    resume1: Optional[AttachmentParams] = None
    resume2: Optional[AttachmentParams] = None
    identity_card_image1: Optional[AttachmentParams] = None
    identity_card_image2: Optional[AttachmentParams] = None
    address_image: Optional[AttachmentParams] = None
    emp_ins_insured_person_number_image: Optional[AttachmentParams] = None
    basic_pension_number_image: Optional[AttachmentParams] = None
    foreign_resident_card_image1: Optional[AttachmentParams] = None
    foreign_resident_card_image2: Optional[AttachmentParams] = None
    handicapped_image: Optional[AttachmentParams] = None
    student_card_image: Optional[AttachmentParams] = None

    bank_accounts: Optional[List[BankAccount]] = None

    @validator('birth_at', 'entered_at', 'resigned_at',
               'first_employment_start_on', 'first_employment_end_on',
               'last_employment_start_on', 'last_employment_end_on',
               pre=True, always=False)
    def validate_date(cls, v):
        if v is not None:
            try:
                datetime.strptime(v, '%Y-%m-%d')
            except ValueError:
                raise ValueError("Date must be in YYYY-MM-DD format")
        return v

class CrewUpdateRequest(CrewCreateRequest):
    pass

# SmartHRClient クラスは変更なし
class SmartHRClient:
    def __init__(self):
        self.base_url = os.getenv('SMARTHR_API_BASE_URL', 'https://app.smarthr.jp/api')
        self.api_key = os.getenv('SMARTHR_API_KEY')
        if not self.api_key:
            raise ValueError("SMARTHR_API_KEY environment variable is not set")

        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def _request(self, method: str, endpoint: str, **kwargs) -> Any:
        """
        SmartHR API に対して共通の HTTP リクエストを送るための内部メソッド

        Args:
            method (str): HTTPメソッド（GET, POST, PUT, PATCH, DELETE）
            endpoint (str): APIエンドポイント（例: /v1/crews）
            **kwargs: requests.request に渡す引数（params, json など）

        Returns:
            Any: APIのレスポンス
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, headers=self.headers, **kwargs)
        if response.status_code == 204:
            return {"status": 204, "message": "No Content"}
        response.raise_for_status()
        return response.json()


    def create_crew(self, crew_data: CrewCreateRequest) -> Dict[str, Any]:
        response = requests.post(
            f'{self.base_url}/v1/crews',
            json=crew_data.dict(exclude_unset=True, exclude_none=True),
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def get_crew(self, crew_id: str, fields: Optional[str] = None) -> Dict[str, Any]:
        params = {}
        if fields:
            params['fields'] = fields

        response = requests.get(
            f'{self.base_url}/v1/crews/{crew_id}',
            params=params,
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def update_crew(self, crew_id: str, crew_data: CrewUpdateRequest) -> Dict[str, Any]:
        response = requests.patch(
            f'{self.base_url}/v1/crews/{crew_id}',
            json=crew_data.dict(exclude_unset=True, exclude_none=True),
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def list_crews(self,
                   page: int = 1,
                   per_page: int = 10,
                   emp_code: Optional[str] = None,
                   emp_type: Optional[EmploymentType] = None,
                   employment_type_id: Optional[str] = None,
                   emp_status: Optional[EmploymentStatus] = None,
                   gender: Optional[Gender] = None,
                   entered_at_from: Optional[str] = None,
                   entered_at_to: Optional[str] = None,
                   resigned_at_from: Optional[str] = None,
                   resigned_at_to: Optional[str] = None,
                   department_id: Optional[str] = None,
                   **kwargs) -> Dict[str, Any]:

        params = {
            'page': page,
            'per_page': per_page
        }

        # Add optional parameters
        if emp_code:
            params['emp_code'] = emp_code
        if emp_type:
            params['emp_type'] = emp_type
        if employment_type_id:
            params['employment_type_id'] = employment_type_id
        if emp_status:
            params['emp_status'] = emp_status
        if gender:
            params['gender'] = gender
        if entered_at_from:
            params['entered_at_from'] = entered_at_from
        if entered_at_to:
            params['entered_at_to'] = entered_at_to
        if resigned_at_from:
            params['resigned_at_from'] = resigned_at_from
        if resigned_at_to:
            params['resigned_at_to'] = resigned_at_to
        if department_id:
            params['department_id'] = department_id

        # Add any additional kwargs
        params.update(kwargs)

        response = requests.get(
            f'{self.base_url}/v1/crews',
            params=params,
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def search_crews(self,
                     query: str,
                     page: int = 1,
                     per_page: int = 10,
                     prefer_business_name: Optional[bool] = None) -> Dict[str, Any]:
        params = {
            'q': query,
            'page': page,
            'per_page': per_page
        }

        if prefer_business_name is not None:
            params['prefer_business_name'] = prefer_business_name

        response = requests.get(
            f'{self.base_url}/v1/crews',
            params=params,
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def invite_crew(self, crew_id: str, inviter_user_id: str, crew_input_form_id: str) -> Dict[str, Any]:
        payload = {}
        if inviter_user_id:
            payload['inviter_user_id'] = inviter_user_id
        if crew_input_form_id:
            payload['crew_input_form_id'] = crew_input_form_id

        response = requests.put(
            f'{self.base_url}/v1/crews/{crew_id}/invite',
            json=payload,
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def delete_crew(self, crew_id: str) -> None:
        response = requests.delete(
            f'{self.base_url}/v1/crews/{crew_id}',
            headers=self.headers
        )
        response.raise_for_status()

    def partial_update_department(self, department_id: str, department_data: DepartmentPartialUpdateRequest) -> Dict[str, Any]:
        """
        指定したIDの部署情報を部分更新します。

        Args:
            department_id (str): 更新する部署のID
            department_data (DepartmentPartialUpdateRequest): 更新する部署の情報

        Returns:
            Dict[str, Any]: 更新された部署の情報
        """
        response = requests.patch(
            f'{self.base_url}/v1/departments/{department_id}',
            json=department_data.dict(exclude_unset=True, exclude_none=True),
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def update_department(self, department_id: str, department_data: DepartmentUpdateRequest) -> Dict[str, Any]:
        """
        指定したIDの部署情報を更新します。

        Args:
            department_id (str): 更新する部署のID
            department_data (DepartmentUpdateRequest): 更新する部署の情報

        Returns:
            Dict[str, Any]: 更新された部署の情報
        """
        response = requests.put(
            f'{self.base_url}/v1/departments/{department_id}',
            json=department_data.dict(exclude_unset=False, exclude_none=False),
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()


    def get_department(self, department_id: str) -> Dict[str, Any]:
        """
        指定したIDの部署情報を取得します。

        Args:
            department_id (str): 取得する部署のID

        Returns:
            Dict[str, Any]: 部署情報
        """
        response = requests.get(
            f'{self.base_url}/v1/departments/{department_id}',
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def list_departments(self,
                          page: int = 1,
                          per_page: int = 10,
                          code: Optional[str] = None,
                          sort: Optional[str] = None) -> Dict[str, Any]:
        """
        部署のリストを取得します。

        Args:
            page (int, optional): 取得するページ番号. Defaults to 1.
            per_page (int, optional): 1ページあたりの結果数. Defaults to 10.
            code (Optional[str], optional): 部署コード. Defaults to None.
            sort (Optional[str], optional): 並び順. Defaults to None.

        Returns:
            Dict[str, Any]: 部署のリスト情報
        """
        params = {
            'page': page,
            'per_page': per_page
        }

        if code:
            params['code'] = code
        if sort:
            params['sort'] = sort

        response = requests.get(
            f'{self.base_url}/v1/departments',
            params=params,
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def create_department(self, department_data: DepartmentCreateRequest) -> Dict[str, Any]:
        """
        新しい部署を作成します。

        Args:
            department_data (DepartmentCreateRequest): 作成する部署の情報

        Returns:
            Dict[str, Any]: 作成された部署の情報
        """
        response = requests.post(
            f'{self.base_url}/v1/departments',
            json=department_data.dict(exclude_unset=True, exclude_none=True),
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def list_employment_types(self, page: int = 1, per_page: int = 10) -> Dict[str, Any]:
        """
        雇用形態のリストを取得します。

        Args:
            page (int, optional): 取得するページ番号. Defaults to 1.
            per_page (int, optional): 1ページあたりの結果数. Defaults to 10.

        Returns:
            Dict[str, Any]: 雇用形態のリスト情報
        """
        params = {
            'page': page,
            'per_page': per_page
        }

        response = requests.get(
            f'{self.base_url}/v1/employment_types',
            params=params,
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def list_employment_types(self, page: int = 1, per_page: int = 10) -> Dict[str, Any]:
        """
        雇用形態のリストを取得します。

        Args:
            page (int, optional): 取得するページ番号. Defaults to 1.
            per_page (int, optional): 1ページあたりの結果数. Defaults to 10.

        Returns:
            Dict[str, Any]: 雇用形態のリスト情報
        """
        params = {
            'page': page,
            'per_page': per_page
        }

    def list_job_titles(self, page: int = 1, per_page: int = 10, sort: Optional[str] = None) -> Dict[str, Any]:
        """
        役職情報のリストを取得します。

        Args:
            page (int, optional): 取得するページ番号. Defaults to 1.
            per_page (int, optional): 1ページあたりの結果数. Defaults to 10.
            sort (Optional[str], optional): 並び順. Defaults to None.

        Returns:
            Dict[str, Any]: 役職情報のリスト
        """
        params = {
            'page': page,
            'per_page': per_page
        }

        if sort:
            params['sort'] = sort

        response = requests.get(
            f'{self.base_url}/v1/job_titles',
            params=params,
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def create_job_title(self, job_title_data: JobTitleCreateRequest) -> Dict[str, Any]:
        """
        新しい役職情報を作成します。

        Args:
            job_title_data (JobTitleCreateRequest): 作成する役職の情報

        Returns:
            Dict[str, Any]: 作成された役職情報
        """
        response = requests.post(
            f'{self.base_url}/v1/job_titles',
            json=job_title_data.dict(exclude_unset=True, exclude_none=True),
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def get_job_title(self, job_title_id: str) -> Dict[str, Any]:
        """
        指定したIDの役職情報を取得します。

        Args:
            job_title_id (str): 取得する役職のID

        Returns:
            Dict[str, Any]: 役職情報
        """
        response = requests.get(
            f'{self.base_url}/v1/job_titles/{job_title_id}',
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def update_job_title(self, job_title_id: str, job_title_data: JobTitleUpdateRequest) -> Dict[str, Any]:
        """
        指定したIDの役職情報を更新します。

        Args:
            job_title_id (str): 更新する役職のID
            job_title_data (JobTitleUpdateRequest): 更新する役職の情報

        Returns:
            Dict[str, Any]: 更新された役職情報
        """
        response = requests.put(
            f'{self.base_url}/v1/job_titles/{job_title_id}',
            json=job_title_data.dict(exclude_unset=False, exclude_none=False),
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def partial_update_job_title(self, job_title_id: str, job_title_data: JobTitlePartialUpdateRequest) -> Dict[str, Any]:
        """
        指定したIDの役職情報を部分更新します。

        Args:
            job_title_id (str): 更新する役職のID
            job_title_data (JobTitlePartialUpdateRequest): 更新する役職の情報

        Returns:
            Dict[str, Any]: 更新された役職情報
        """
        response = requests.patch(
            f'{self.base_url}/v1/job_titles/{job_title_id}',
            json=job_title_data.dict(exclude_unset=True, exclude_none=True),
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def delete_job_title(self, job_title_id: str) -> None:
        """
        指定したIDの役職情報を削除します。

        Args:
            job_title_id (str): 削除する役職のID
        """
        response = requests.delete(
            f'{self.base_url}/v1/job_titles/{job_title_id}',
            headers=self.headers
        )
        response.raise_for_status()

        response = requests.get(
            f'{self.base_url}/v1/employment_types',
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def discontinue_department(self, department_id: str, discontinued_date: str) -> Dict[str, Any]:
        """
        指定したIDの部署を廃止します。

        Args:
            department_id (str): 廃止する部署のID
            discontinued_date (str): 廃止日（YYYY-MM-DD）※過去日でなければならない

        Returns:
            Dict[str, Any]: 結果ステータス
        """

        # 日付をチェック（昨日以前であること）
        today = datetime.today().date()
        target_date = datetime.strptime(discontinued_date, "%Y-%m-%d").date()
        if target_date >= today:
            raise ValueError("廃止日は本日または未来日にはできません。昨日以前の日付を指定してください。")

        payload = DepartmentDiscontinueRequest(discontinued_date=discontinued_date)

        response = requests.post(
            f'{self.base_url}/v1/departments/{department_id}/discontinue',
            json=payload.dict(),
            headers=self.headers
        )
        response.raise_for_status()

        return {
            "status": response.status_code,
            "message": "Department discontinued successfully"
        }

    def create_employment_type(self, employment_type_data: EmploymentTypeCreateRequest) -> Dict[str, Any]:
        """
        新しい雇用形態を作成します。

        Args:
            employment_type_data (EmploymentTypeCreateRequest): 作成する雇用形態の情報

        Returns:
            Dict[str, Any]: 作成された雇用形態の情報
        """
        response = requests.post(
            f'{self.base_url}/v1/employment_types',
            json=employment_type_data.dict(exclude_unset=True, exclude_none=True),
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def get_employment_type(self, employment_type_id: str) -> Dict[str, Any]:
        """
        指定したIDの雇用形態情報を取得します。

        Args:
            employment_type_id (str): 取得する雇用形態のID

        Returns:
            Dict[str, Any]: 雇用形態情報
        """
        response = requests.get(
            f'{self.base_url}/v1/employment_types/{employment_type_id}',
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def update_employment_type(self, employment_type_id: str, employment_type_data: EmploymentTypeUpdateRequest) -> Dict[str, Any]:
        """
        指定したIDの雇用形態情報を更新します。

        Args:
            employment_type_id (str): 更新する雇用形態のID
            employment_type_data (EmploymentTypeUpdateRequest): 更新する雇用形態の情報

        Returns:
            Dict[str, Any]: 更新された雇用形態の情報
        """
        response = requests.put(
            f'{self.base_url}/v1/employment_types/{employment_type_id}',
            json=employment_type_data.dict(exclude_unset=False, exclude_none=False),
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def partial_update_employment_type(self, employment_type_id: str, employment_type_data: EmploymentTypePartialUpdateRequest) -> Dict[str, Any]:
        """
        指定したIDの雇用形態情報を部分更新します。

        Args:
            employment_type_id (str): 更新する雇用形態のID
            employment_type_data (EmploymentTypePartialUpdateRequest): 更新する雇用形態の情報

        Returns:
            Dict[str, Any]: 更新された雇用形態の情報
        """
        response = requests.patch(
            f'{self.base_url}/v1/employment_types/{employment_type_id}',
            json=employment_type_data.dict(exclude_unset=True, exclude_none=True),
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def delete_employment_type(self, employment_type_id: str) -> None:
        """
        指定したIDの雇用形態情報を削除します。

        Args:
            employment_type_id (str): 削除する雇用形態のID
        """
        response = requests.delete(
            f'{self.base_url}/v1/employment_types/{employment_type_id}',
            headers=self.headers
        )
        response.raise_for_status()

    def delete_employment_type(self, employment_type_id: str) -> None:
        """
        指定したIDの雇用形態情報を削除します。

        Args:
            employment_type_id (str): 削除する雇用形態のID
        """
        response = requests.delete(
            f'{self.base_url}/v1/employment_types/{employment_type_id}',
            headers=self.headers
        )
        response.raise_for_status()

    def list_grades(self, page: int = 1, per_page: int = 10, sort: Optional[str] = None) -> Dict[str, Any]:
        """
        等級のリストを取得します。

        Args:
            page (int, optional): 取得するページ番号. Defaults to 1.
            per_page (int, optional): 1ページあたりの結果数. Defaults to 10.
            sort (Optional[str], optional): 並び順. Defaults to None.

        Returns:
            Dict[str, Any]: 等級のリスト情報
        """
        params = {
            'page': page,
            'per_page': per_page
        }
        if sort:
            params['sort'] = sort

        response = requests.get(
            f'{self.base_url}/v1/grades',
            params=params,
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def create_grade(self, grade_data: GradeCreateRequest) -> Dict[str, Any]:
        """
        新しい等級を作成します。

        Args:
            grade_data (GradeCreateRequest): 作成する等級の情報

        Returns:
            Dict[str, Any]: 作成された等級の情報
        """
        response = requests.post(
            f'{self.base_url}/v1/grades',
            json=grade_data.dict(exclude_unset=True, exclude_none=True),
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def get_grade(self, grade_id: str) -> Dict[str, Any]:
        """
        指定したIDの等級情報を取得します。

        Args:
            grade_id (str): 取得する等級のID

        Returns:
            Dict[str, Any]: 等級情報
        """
        response = requests.get(
            f'{self.base_url}/v1/grades/{grade_id}',
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def update_grade(self, grade_id: str, grade_data: GradeUpdateRequest) -> Dict[str, Any]:
        """
        指定したIDの等級情報を更新します。

        Args:
            grade_id (str): 更新する等級のID
            grade_data (GradeUpdateRequest): 更新する等級の情報

        Returns:
            Dict[str, Any]: 更新された等級の情報
        """
        response = requests.put(
            f'{self.base_url}/v1/grades/{grade_id}',
            json=grade_data.dict(exclude_unset=True, exclude_none=True),
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def partial_update_grade(self, grade_id: str, grade_data: GradePartialUpdateRequest) -> Dict[str, Any]:
        """
        指定したIDの等級情報を部分更新します。

        Args:
            grade_id (str): 更新する等級のID
            grade_data (GradePartialUpdateRequest): 部分更新する等級の情報

        Returns:
            Dict[str, Any]: 更新された等級の情報
        """
        response = requests.patch(
            f'{self.base_url}/v1/grades/{grade_id}',
            json=grade_data.dict(exclude_unset=True, exclude_none=True),
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def delete_grade(self, grade_id: str) -> None:
        """
        指定したIDの等級情報を削除します。

        Args:
            grade_id (str): 削除する等級のID
        """
        response = requests.delete(
            f'{self.base_url}/v1/grades/{grade_id}',
            headers=self.headers
        )

    def list_job_categories(self, page: int = 1, per_page: int = 10, sort: Optional[str] = None) -> Dict[str, Any]:
        """
        職種のリストを取得します。

        Args:
            page (int, optional): 取得するページ番号. Defaults to 1.
            per_page (int, optional): 1ページあたりの結果数. Defaults to 10.
            sort (Optional[str], optional): 並び順. Defaults to None.

        Returns:
            Dict[str, Any]: 職種のリスト情報
        """
        params = {
            'page': page,
            'per_page': per_page
        }
        if sort:
            params['sort'] = sort

        return self._request("GET", "/v1/job_categories", params=params)

    def create_job_category(self, job_category_data: JobCategoryCreateRequest) -> Dict[str, Any]:
        """
        新しい職種を作成します。

        Args:
            job_category_data (JobCategoryCreateRequest): 作成する職種の情報

        Returns:
            Dict[str, Any]: 作成された職種の情報
        """
        return self._request("POST", "/v1/job_categories", json=job_category_data.dict(exclude_unset=True, exclude_none=True))

    def get_job_category(self, job_category_id: str) -> Dict[str, Any]:
        """
        指定したIDの職種情報を取得します。

        Args:
            job_category_id (str): 取得する職種のID

        Returns:
            Dict[str, Any]: 職種情報
        """
        return self._request("GET", f"/v1/job_categories/{job_category_id}")

    def list_dependents(self, crew_id: str, page: int = 1, per_page: int = 10, **kwargs) -> Dict[str, Any]:
        """
        指定した従業員の家族情報のリストを取得します。

        Args:
            crew_id (str): 従業員ID
            page (int, optional): 取得するページ番号. Defaults to 1.
            per_page (int, optional): 1ページあたりの結果数. Defaults to 10.

        Returns:
            Dict[str, Any]: 家族情報のリスト
        """
        params = {
            "page": page,
            "per_page": per_page,
            **kwargs
        }
        try:
            response = self._request("GET", f"/v1/crews/{crew_id}/dependents", params=params)

            if isinstance(response, dict) and response.get("dependents") == []:
                return {
                    "message": "この従業員には家族情報が登録されていません。",
                    "dependents": []
                }

            return response

        except Exception as e:
            print(f"[ERROR] list_dependents failed: {e}")
            raise

    def create_dependent(self, crew_id: str, dependent_data: DependentCreateRequest) -> Dict[str, Any]:
        """
        指定した従業員の家族情報を新規作成します。

        Args:
            crew_id (str): 従業員ID
            dependent_data (DependentCreateRequest): 作成する家族情報

        Returns:
            Dict[str, Any]: 作成された家族情報
        """
        return self._request(
                "POST",
                f"/v1/crews/{crew_id}/dependents",
                json=dependent_data.dict(exclude_none=True)
            )

    def get_dependent(self, crew_id: str, dependent_id: str) -> Dict[str, Any]:
        """
        指定した従業員の特定の家族情報を取得します。

        Args:
            crew_id (str): 従業員ID
            dependent_id (str): 家族情報ID

        Returns:
            Dict[str, Any]: 家族情報
        """
        return self._request("GET", f"/v1/crews/{crew_id}/dependents/{dependent_id}")

    def update_dependent(self, crew_id: str, dependent_id: str, dependent_data: DependentUpdateRequest) -> Dict[str, Any]:
        """
        指定した従業員の家族情報を更新します。

        Args:
            crew_id (str): 従業員ID
            dependent_id (str): 家族情報ID
            dependent_data (DependentUpdateRequest): 更新する家族情報

        Returns:
            Dict[str, Any]: 更新された家族情報
        """
        return self._request("PUT", f"/v1/crews/{crew_id}/dependents/{dependent_id}", json=dependent_data.dict(exclude_unset=True, exclude_none=True))

    def partial_update_dependent(self, crew_id: str, dependent_id: str, dependent_data: DependentPartialUpdateRequest) -> Dict[str, Any]:
        """
        指定した従業員の家族情報を部分更新します。

        Args:
            crew_id (str): 従業員ID
            dependent_id (str): 家族情報ID
            dependent_data (DependentPartialUpdateRequest): 部分更新する家族情報

        Returns:
            Dict[str, Any]: 更新された家族情報
        """
        if not dependent_data.has_required_patch_fields():
            raise ValueError("家族情報の部分更新には、姓・名・性別・生年月日・続柄ID・同居区分が必須です。")

        try:
            return self._request("PATCH", f"/v1/crews/{crew_id}/dependents/{dependent_id}", json=dependent_data.dict(exclude_unset=True, exclude_none=True))

        except requests.HTTPError as e:
            print(f"[ERROR] 家族情報の部分更新失敗: {e.response.text}")
            raise

    def delete_dependent(self, crew_id: str, dependent_id: str) -> None:
        """
        指定した従業員の家族情報を削除します。

        Args:
            crew_id (str): 従業員ID
            dependent_id (str): 家族情報ID
        """
        self._request("DELETE", f"/v1/crews/{crew_id}/dependents/{dependent_id}")

    def list_relations(self, page: int = 1, per_page: int = 100) -> List[Dict[str, Any]]:
        """
        続柄のリストを取得します。

        Args:
            page (int): ページ番号（デフォルトは1）
            per_page (int): 1ページあたりの取得件数（デフォルトは100）

        Returns:
            List[Dict[str, Any]]: 続柄のリスト
        """
        url = f"{self.base_url}/v1/dependent_relations"
        params = {"page": page, "per_page": per_page}
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()