from pathlib import Path
from autoqemu.dumper import connect, dump_client
import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="autoqemu", description="Launches kernels and dumps the memory image"
    )
    parser.add_argument(
        "-k",
        "--kernel",
        type=Path,
        help="The bzImage used to launch the kernel",
        required=True,
    )
    parser.add_argument(
        "-r",
        "--rootfs",
        type=Path,
        help="The initrd root filesystem to boot from",
        required=True,
    )
    parser.add_argument(
        "-f",
        "--dump-file",
        type=Path,
        help="Where to dump the file",
        default=Path("./memory_dump.img"),
    )
    parser.add_argument(
        "-s",
        "--qmp-socket",
        help="The socket to run the QMP server on",
        default="qmp.sock",
    )
    parser.add_argument(
        "-n",
        "--qmp-nickname",
        help="The name of the qmp connection client",
        default="qmp-dld",
    )
    return parser.parse_args()


def main() -> None:
    print("Hello from autoqemu!")
    args = parse_args()
    qmp_client = connect(args.qmp_nickname, args.qmp_socket)
    dump_client(qmp_client, args.dump_file)
