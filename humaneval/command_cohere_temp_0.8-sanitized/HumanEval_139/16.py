import multiprocessing
def special_factorial(n):
    pool = multiprocessing.Pool(processes=None)
    partial_products = pool.map(lambda x: x * (x - 1), range(2, n + 1))
    result = 1
    for partial_product in partial_products:
        result *= partial_product
    pool.close()
    return result