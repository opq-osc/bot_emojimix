from typing import List, Optional

import httpx

try:
    from .emojis import emojis
except ImportError:
    from emojis import emojis


emoji_to_codes = lambda c: list(map(lambda x: ord(x), c))  # type: (str) -> List[int]
codes_to_unicode = lambda codes: "-".join(
    list(map(lambda code: f"u{code:x}", codes))
)  # type: (List[int]) -> str


def mix_emoji(emoji_1: str, emoji_2: str) -> Optional[bytes]:
    codes_1 = emoji_to_codes(emoji_1)

    try:
        path = emojis["-".join([str(i) for i in codes_1])]
    except KeyError:
        return

    unicode_1 = codes_to_unicode(codes_1)
    unicode_2 = codes_to_unicode(emoji_to_codes(emoji_2))

    url = f"https://www.gstatic.com/android/keyboard/emojikitchen/{path}/{unicode_1}/{unicode_1}_{unicode_2}.png"
    try:
        resp = httpx.get(url, timeout=10)
        resp.raise_for_status()
    except Exception:
        return
    else:
        return resp.content


def help() -> str:
    chars = []
    for code in emojis.keys():
        items = [chr(int(i)) for i in code.split('-')]
        chars.append(''.join(items))

    return '支持的emoji有：' + ', '.join(chars)
