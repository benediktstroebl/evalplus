

def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    # open_brackets = {"<": ">"}
    # close_brackets = {">": "<"}
    # 需要建立一个字典，两个key一样，每个value也一样，有点困扰，需要找到不同的方法
    #
    # brackets_dict = {"<": ">", ">": "<"}
    #
    # for key, value in brackets_dict.items():
    #     if key in brackets and value in brackets:
    #         print(f"{key} and {value}")
    #
    # for key in brackets_dict.keys():
    #     if key in brackets and brackets_dict[key] in brackets:
    #         print(f"{key} and {brackets_dict[key]}")
    #
    # for key in brackets_dict.values():
    #     if key in brackets and brackets_dict[key] in brackets:
    #         print(f"
