from app import create_app
from app.config import Config
import sys

# 验证配置
errors = Config.validate()
if errors:
    print("配置错误:")
    for err in errors:
        print(f"  - {err}")
    print("\n请检查 .env 文件或环境变量中的配置")
    sys.exit(1)

# 为Gunicorn暴露app对象
app = create_app()
