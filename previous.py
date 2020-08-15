def prev(number, base):
    # base = 5
    temp = (math.ceil(number / base) * base) - base
    return temp
    
def anotherPrev(number, base):
    # base = 5
    temp = round((number - (base - 1)) / base) * base
    return temp
