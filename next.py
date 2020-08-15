def next(number, base):
    # base = 5
    temp = math.ceil(number / base) * base
    return temp
    
def anotherNext(number, base):
    # base = 5
    temp = round((number + (base-1)) / base) * base
    return temp
