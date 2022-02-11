"""emoji合成
使用举例：发送 🥳+👑
"""
from botoy import GroupMsg, S
from botoy.decorators import ignore_botself, on_regexp

try:
    from .emojimix import mix_emoji
except ImportError:
    from emojimix import mix_emoji


@ignore_botself
@on_regexp(r"^([\u200d-\U0001fab5]+)\+([\u200d-\U0001fab5]+)$")
def receive_group_msg(ctx: GroupMsg):
    emoji_1, emoji_2 = ctx._match[1], ctx._match[2]

    data = None

    for i in ((emoji_1, emoji_2), (emoji_2, emoji_1)):

        ret = mix_emoji(*i)
        if ret:
            data = ret
            break

    if data:
        S.image(data)
