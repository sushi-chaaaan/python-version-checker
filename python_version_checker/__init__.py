import sys

from typing import Optional


def python_ver_is_over(major: int, minor: Optional[int] = None, micro: Optional[int] = None) -> bool:
    """
    Checks if the Python version is greater than the one specified in the argument.

    if the minor version is not specified, it checks only the major version.

    if the micro version is not specified, it checks only the major and minor versions.

    Args:
        major (:obj:`int`): the major version number
        minor (:obj:`Optional[int]`): the minor version number. Defaults to None.
        micro (:obj:`Optional[int]`): the micro version number. Defaults to None.

    Returns:
        bool: `True` if the Python version is greater than the one specified in the argument.
    """
    if minor is None:
        return sys.version_info[0] > major
    elif micro is None:
        return sys.version_info[0] > major or sys.version_info[1] > minor
    else:
        return sys.version_info[0] > major or sys.version_info[1] > minor or sys.version_info[2] > micro


def python_ver_is_over_or_eq(major: int, minor: Optional[int] = None, micro: Optional[int] = None) -> bool:
    """
    Checks if the Python version is greater than or equal to the one specified in the argument.

    if the minor version is not specified, it checks only the major version.

    if the micro version is not specified, it checks only the major and minor versions.

    Args:
        major (:obj:`int`): the major version number
        minor (:obj:`Optional[int]`): the minor version number. Defaults to None.
        micro (:obj:`Optional[int]`): the micro version number. Defaults to None.

    Returns:
        bool: `True` if the Python version is greater than or equal to the one specified in the argument.
    """
    if minor is None:
        return sys.version_info[0] >= major
    elif micro is None:
        return sys.version_info[0] >= major or sys.version_info[1] >= minor
    else:
        return sys.version_info[0] >= major or sys.version_info[1] >= minor or sys.version_info[2] >= micro


def python_ver_is(major: int, minor: Optional[int] = None, micro: Optional[int] = None) -> bool:
    """
    Checks if the Python version is equal to the one specified in the argument.

    if the minor version is not specified, it checks only the major version.

    if the micro version is not specified, it checks only the major and minor versions.

    Args:
        major (:obj:`int`): the major version number
        minor (:obj:`Optional[int]`): the minor version number. Defaults to None.
        micro (:obj:`Optional[int]`): the micro version number. Defaults to None.

    Returns:
        bool: `True` if the Python version is equal to the one specified in the argument.
    """
    if minor is None:
        return sys.version_info[0] == major
    elif micro is None:
        return sys.version_info[0] == major and sys.version_info[1] == minor
    else:
        return sys.version_info[0] == major and sys.version_info[1] == minor and sys.version_info[2] == micro


def python_ver_is_under(major: int, minor: Optional[int] = None, micro: Optional[int] = None) -> bool:
    """
    Checks if the Python version is less than the one specified in the argument.

    if the minor version is not specified, it checks only the major version.

    if the micro version is not specified, it checks only the major and minor versions.

    Args:
        major (:obj:`int`): the major version number
        minor (:obj:`Optional[int]`): the minor version number. Defaults to None.
        micro (:obj:`Optional[int]`): the micro version number. Defaults to None.

    Returns:
        bool: `True` if the Python version is less than the one specified in the argument.
    """
    if minor is None:
        return sys.version_info[0] < major
    elif micro is None:
        return sys.version_info[0] < major or sys.version_info[1] < minor
    else:
        return sys.version_info[0] < major or sys.version_info[1] < minor or sys.version_info[2] < micro


def python_ver_is_under_or_eq(major: int, minor: Optional[int] = None, micro: Optional[int] = None) -> bool:
    """
    Checks if the Python version is less than or equal to the one specified in the argument.

    if the minor version is not specified, it checks only the major version.

    if the micro version is not specified, it checks only the major and minor versions.

    Args:
        major (:obj:`int`): the major version number
        minor (:obj:`Optional[int]`): the minor version number. Defaults to None.
        micro (:obj:`Optional[int]`): the micro version number. Defaults to None.

    Returns:
        bool: `True` if the Python version is less than or equal to the one specified in the argument.
    """
    if minor is None:
        return sys.version_info[0] <= major
    elif micro is None:
        return sys.version_info[0] <= major or sys.version_info[1] <= minor
    else:
        return sys.version_info[0] <= major or sys.version_info[1] <= minor or sys.version_info[2] <= micro
