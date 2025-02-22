import platform
from pathlib import Path
from typing import Optional

from .utils import ConfigsManager

if platform.system() == "Linux":
    import os

    hostip = (
        os.popen("cat /etc/resolv.conf | grep nameserver | awk '{ print $2 }'")
        .read()
        .replace("\n", "")
    )


# 回复消息名称
NICKNAME: str = "小真寻"

# 数据库（必要）
# 如果填写了bind就不需要再填写后面的字段了#）
# 示例："bind": "postgres://user:password@127.0.0.1:5432/database"
bind: str = ""  # 数据库连接链接
sql_name: str = "postgres"
user: str = "postgres"
password: str = "dadagua"
address: str = "127.0.0.1"
port: str = "5432"
database: str = "大大呱"

# 代理，例如 "http://127.0.0.1:7890"
# 如果是WLS 可以 f"http://{hostip}:7890" 使用寄主机的代理
SYSTEM_PROXY: Optional[str] = None  # 全局代理


Config = ConfigsManager(Path() / "data" / "configs" / "plugins2config.yaml")
