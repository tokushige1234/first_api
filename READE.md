### start project

```bash
#1. 仮想環境の作成
python -m venv .venv 
#2. 仮想環境の有効化
. .venv/bin/activate 
#3. djangoのインストール
pip install django
#4. djangoプロジェクトの作成
django-admin startproject rest_project .
#5. サーバーの起動
python manage.py runserver
#6 アプリケーションの作成
python manage.py startapp api
# django rest frameworkのインストール（プロジェクト内で実行）
pip install djangorestframework

