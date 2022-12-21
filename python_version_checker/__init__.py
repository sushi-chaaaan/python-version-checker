import sys


def python_ver_is_over(
    major: int, minor: int | None = None, micro: int | None = None
) -> bool:
    if minor is None:
        return sys.version_info[0] > major
    elif micro is None:
        return sys.version_info[0] > major or sys.version_info[1] > minor
    else:
        return (
            sys.version_info[0] > major
            or sys.version_info[1] > minor
            or sys.version_info[2] > micro
        )


def python_ver_is_over_or_eq(
    major: int, minor: int | None = None, micro: int | None = None
) -> bool:
    if minor is None:
        return sys.version_info[0] >= major
    elif micro is None:
        return sys.version_info[0] >= major or sys.version_info[1] >= minor
    else:
        return (
            sys.version_info[0] >= major
            or sys.version_info[1] >= minor
            or sys.version_info[2] >= micro
        )


def python_ver_is(
    major: int, minor: int | None = None, micro: int | None = None
) -> bool:
    if minor is None:
        return sys.version_info[0] == major
    elif micro is None:
        return sys.version_info[0] == major and sys.version_info[1] == minor
    else:
        return (
            sys.version_info[0] == major
            and sys.version_info[1] == minor
            and sys.version_info[2] == micro
        )


def python_ver_is_under(
    major: int, minor: int | None = None, micro: int | None = None
) -> bool:
    if minor is None:
        return sys.version_info[0] < major
    elif micro is None:
        return sys.version_info[0] < major or sys.version_info[1] < minor
    else:
        return (
            sys.version_info[0] < major
            or sys.version_info[1] < minor
            or sys.version_info[2] < micro
        )


def python_ver_is_under_or_eq(major: int, minor: int, micro: int) -> bool:
    if minor is None:
        return sys.version_info[0] <= major
    elif micro is None:
        return sys.version_info[0] <= major or sys.version_info[1] <= minor
    else:
        return (
            sys.version_info[0] <= major
            or sys.version_info[1] <= minor
            or sys.version_info[2] <= micro
        )
