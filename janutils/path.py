import pathlib
import re
from typing import Optional, Union

def get_first_item(root: Union[pathlib.Path, str], *fragments: Optional[str]) -> pathlib.Path:
    current = pathlib.Path(root)
    if not fragments:
        fragments = (None,)
    for fragment in fragments:
        for item in current.iterdir():
            if fragment is None:
                current = item
                break
            elif re.match(fragment, item.name):
                current = item
                break
        else:
            raise ValueError(f"Fragment {fragment} not found in {current}")
    return current