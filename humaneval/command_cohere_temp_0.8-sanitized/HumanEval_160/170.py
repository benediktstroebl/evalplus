def do_algebra(operator, operand):
    num_operands = len(operand)
    expr_str = ''
    
    for i in range(num_operands - 1):
        expr_str += f'{operand[i]} {operator[i]} '
    
    expr_str += f'{operand[-1]} '
    
    for op in operator:
        if op == '+':
            result = eval(expr_str) + eval(f'{operand[-1]} {op} 0')
        elif op == '-':
            result = eval(expr_str) - eval(f'{operand[-1]} {op} 0')
        elif op == '*':
            result = eval(expr_str) * eval(f'{operand[-1]} {op} 0')
        elif op == '//':
            result = eval(expr_str) // eval(f'{operand[-1]} {op} 0')
        elif op == '**':
            result = eval(expr_str) ** eval(f'{operand[-1]} {op} 0')
        else:
            return 'Error: Invalid operator ' + op + ' in the expression'
    
    return result
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
result = do_algebra(operator, operand)