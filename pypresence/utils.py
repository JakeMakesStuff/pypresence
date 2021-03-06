import asyncio
# Util functions that are needed but messy.


def remove_none(d: dict): # Made by https://github.com/LewdNeko ;^)
    for item in d.copy():
        if isinstance(d[item], dict):
            if len(d[item]):
                d[item] = remove_none(d[item])
            else:
                del d[item]
        elif d[item] is None:
            del d[item]
    return d


try: # Thanks, Rapptz :^)
    create_task = asyncio.ensure_future
except AttributeError:
    create_task = eval(
        "asyncio.async"
    )
    # No longer crashes Python 3.7.
    # Fix by JakeMakesStuff.
