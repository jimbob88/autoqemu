from pathlib import Path
from subprocess import Popen, PIPE
import shutil


def start_proc(bz_image: Path, root_filesystem: Path, socket: str) -> Popen:
    qemu = shutil.which("qemu-system-x86_64")
    if qemu is None:
        raise ValueError("Could not find qemu")

    return Popen(
        [
            qemu,
            "-kernel",
            bz_image,
            "-drive",
            f"file={root_filesystem},format=raw",
            "-snapshot",
            "-nographic",
            "-monitor",
            "/dev/null",
            "-no-reboot",
            "-smp",
            "1",
            "-append",
            "root=/dev/sda rw init=/init console=ttyS0 nokaslr nopti loglevel=3 oops=panic panic=-1",
            "-enable-kvm",
            "-m",
            "256M",
            "-cpu",
            "qemu64",
            "-qmp",
            f"unix:{socket},server=on,wait=off",
        ],
        stdout=PIPE,
    )
