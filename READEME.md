# Bitly clone 專案

## 專案初始化

- ==步驟 1: 創建虛擬環境== env/

```python
python3 -m venv env
```

- ==步驟 2: 啟用虛擬環境==

```python
source env/bin/activate # 停用 => deactivate
```

- ==步驟 3: 安裝 django==

```python
pip3 install django
```

- ==步驟 4: 專案的應用程式目錄配置==

```python
django-admin startproject config .
```

- ==步驟 5: 運行應用程式==

```python
python3 manage.py runserver
```

- 步驟 6: 創建 app links

```python
django-admin startapp links
```
