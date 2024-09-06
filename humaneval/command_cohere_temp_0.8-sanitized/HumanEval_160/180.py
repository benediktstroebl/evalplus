def do_algebra(operator, operand):
    assert len(operator) == len(operand) - 1, "Operator list length must be equal to operand list length - 1"
    assert len(operator) > 0 and len(operand) > 1, "Operator list must have at least one element and operand list must have at least two elements"
    
    result = 0
    for i in range(len(operand) - 1):
        result += operator[i] * operand[i+1]
    
    return result