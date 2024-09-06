def do_algebra(operator, operand):
    result = 0
    oper_len = len(operator)
    expect = len(operand) - 1
    assert oper_len == expect, "operators length should be equal to expect length - 1"
    assert oper_len > 0 and expect > 1, "must provide at least one operator and two operands"

    # go through operand list and use corresponding operator to create expression and evaluate it
    for i in range(expect):
        try:
            exp = eval(operator[i] + " " + str(operand[i]))
        except ZeroDivisionError:
            continue
        except Exception as e:
            print(e)
        result += exp
    return result