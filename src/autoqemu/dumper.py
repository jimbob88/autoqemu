from pathlib import Path
from qemu.qmp import QMPClient


async def connect(nickname: str, socket: str) -> QMPClient:
    qmp = QMPClient(nickname)
    await qmp.connect(socket)
    return qmp


async def dump_client(client: QMPClient, out_file: Path) -> dict:
    return await client.execute(
        "dump-guest-memory",
        arguments={"paging": False, "protocol": f"file:{out_file.absolute()}"},
    )
