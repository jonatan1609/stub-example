from typing import Union


def x(
        name: str,
        last_name: str = None,
        address: str = None
) -> Union[str, bool]:
    if address:
        return True
    elif last_name:
        return last_name
    return name
