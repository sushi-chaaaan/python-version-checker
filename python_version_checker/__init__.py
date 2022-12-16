def python_ver_is_over(major: int, minor: int, micro: int) -> bool:
    import sys

    return sys.version_info >= (major, minor, micro)


def python_ver_is(major: int, minor: int, micro: int) -> bool:
    import sys

    return sys.version_info == (major, minor, micro)


def python_ver_is_under(major: int, minor: int, micro: int) -> bool:
    import sys

    return sys.version_info <= (major, minor, micro)
