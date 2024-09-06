def fib4(n):
    a,b,c,d = 0,0,1,0
    for i in range(n):
        a,b,c,d = d,a+b,c+d,a+b+c+d
    return d
    # -------------------------------------------------------
    # NOTE: The following constants are Fib4 values at specific indices.
    # They're included to allow testing the function above WITH VALUES
    # KNOWN TO BE CORRECT. If you're solving this problem on a platform
    # WHERE IMPORTING CONSTANTS IS ACCEPTABLE, you can import these values
    # to verify that your function is correctly calculating Fib4 values.
    # -------------------------------------------------------
    # import sys
    # sys.stdout.buffer.write(__file__.encode('ascii')[:-1])
    # sys.stdout.buffer.write(b"\n")
    # sys.stdout.buffer.write(str(fib4(0)).encode('ascii'))
    # sys.stdout.buffer.write(b"\n")
    # sys.stdout.buffer.write(str(fib4(1)).encode('ascii'))
    # sys.stdout.buffer.write(b"\n")
    # sys.stdout.buffer.write(str(fib4(2)).encode('ascii'))
    # sys.stdout.buffer.write(b"\n")
    # sys.stdout.buffer.write(str(fib4(3)).encode('ascii'))
    # sys.stdout.buffer.write(b"\n")
    # sys.stdout.buffer.write(str(fib4(4)).encode('ascii'))
    # sys.stdout.buffer.write(b"\n")
    # sys.stdout.buffer.write(str(fib4(5)).encode('ascii'))
    # sys.stdout.buffer.write(b"\n")
    # sys.stdout.buffer.write(str(fib4(6)).encode('ascii'))
    # sys.stdout.buffer.write(b"\n")
    # sys.stdout.buffer.write(str(fib4(7)).encode('ascii'))