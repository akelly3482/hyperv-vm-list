"""HyperV VM List — List Hyper-V virtual machines with state and generation, if the role is installed."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='hyperv_vm_list',
        description='List Hyper-V virtual machines with state and generation, if the role is installed.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('HyperV VM List')
    print('What VMs are on this box.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
