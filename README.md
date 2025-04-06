# SmartHR MCP Server

このプロジェクトは、[SmartHR API](https://developer.smarthr.jp/) に対応した MCP (Model Context Protocol) サーバーです。
SmartHR の従業員・部署・役職・雇用形態・等級などの情報を MCP ツールとして扱うことができます。

## 構成

```
smarthr-mcp-server/
│
├── .env_sample
├── .gitignore
├── main.py
├── pyproject.toml
├── README.md
├── requirements.txt
├── smarthr_mcp_server.json         # MCP ツールとしての定義とコマンド情報（MCP 対応クライアント用）
├── uv.lock
│
└── smarthr_mcp_server/
    ├── server.py                   # FastMCP ベースの MCP サーバー実装
    ├── smarthr_client.py          # SmartHR API との通信を担当するクライアントモジュール
    └── smarthr_mcp_server.egg-info/
```

## 環境変数（.env）

SmartHR API との通信には以下の環境変数が必要です。

```env
SMARTHR_API_BASE_URL=https://app.smarthr.jp/api
SMARTHR_API_KEY=YOUR_SMARTHR_API_TOKEN
```

## 使い方

1. **リポジトリをクローンまたはダウンロード**
2. **環境変数の設定（.env）**
3. **Claude for Desktop の設定**

   `claud_desktop_config.json` に smarthr_mcp_server.json の内容を追記

4. **Claude for Desktop の再起動**

   ```
   % killall "Claude"
   % open -a Claude
   ```

## 対応ツール一覧

#### 登録 関連

| 関数名                             | 説明     |
| ---------------------------------- | -------- |
| `smarthr_create_crew()`            | 従業員   |
| `smarthr_create_department()`      | 部署     |
| `smarthr_create_dependent()`       | 家族情報 |
| `smarthr_create_employment_type()` | 雇用形態 |
| `smarthr_create_grade()`           | 等級     |
| `smarthr_create_job_category()`    | 職種     |
| `smarthr_create_job_title()`       | 役職     |

#### 削除 関連

| 関数名                             | 説明     |
| ---------------------------------- | -------- |
| `smarthr_delete_crew()`            | 従業員   |
| `smarthr_delete_dependent()`       | 家族情報 |
| `smarthr_delete_employment_type()` | 雇用形態 |
| `smarthr_delete_grade()`           | 等級     |
| `smarthr_delete_job_category()`    | 職種     |
| `smarthr_delete_job_title()`       | 役職     |

#### 廃止 関連

| 関数名                             | 説明 |
| ---------------------------------- | ---- |
| `smarthr_discontinue_department()` | 部署 |

#### 取得 関連

| 関数名                          | 説明     |
| ------------------------------- | -------- |
| `smarthr_get_crew()`            | 従業員   |
| `smarthr_get_department()`      | 部署     |
| `smarthr_get_dependent()`       | 家族情報 |
| `smarthr_get_employment_type()` | 雇用形態 |
| `smarthr_get_grade()`           | 等級     |
| `smarthr_get_job_category()`    | 職種     |
| `smarthr_get_job_title()`       | 役職     |

#### 招待 関連

| 関数名                  | 説明   |
| ----------------------- | ------ |
| `smarthr_invite_crew()` | 従業員 |

#### リスト取得 関連

| 関数名                            | 説明     |
| --------------------------------- | -------- |
| `smarthr_list_crews()`            | 従業員   |
| `smarthr_list_departments()`      | 部署     |
| `smarthr_list_dependents()`       | 家族情報 |
| `smarthr_list_employment_types()` | 雇用形態 |
| `smarthr_list_grades()`           | 等級     |
| `smarthr_list_job_categories()`   | 職種     |
| `smarthr_list_job_titles()`       | 役職     |
| `smarthr_list_relations()`        | 続柄     |

#### 部分更新 関連

| 関数名                                     | 説明     |
| ------------------------------------------ | -------- |
| `smarthr_partial_update_department()`      | 部署     |
| `smarthr_partial_update_dependent()`       | 家族情報 |
| `smarthr_partial_update_employment_type()` | 雇用形態 |
| `smarthr_partial_update_grade()`           | 等級     |
| `smarthr_partial_update_job_category()`    | 職種     |
| `smarthr_partial_update_job_title()`       | 役職     |

#### 検索 関連

| 関数名                   | 説明   |
| ------------------------ | ------ |
| `smarthr_search_crews()` | 従業員 |

#### 更新 関連

| 関数名                             | 説明     |
| ---------------------------------- | -------- |
| `smarthr_update_crew()`            | 従業員   |
| `smarthr_update_department()`      | 部署     |
| `smarthr_update_dependent()`       | 家族情報 |
| `smarthr_update_employment_type()` | 雇用形態 |
| `smarthr_update_grade()`           | 等級     |
| `smarthr_update_job_category()`    | 職種     |
| `smarthr_update_job_title()`       | 役職     |

## ライセンス

MIT

## 免責事項

本プログラムを利用して行う一切の行為、被った損害・損失に対しては、一切の責任を負いかねます。
