def q_number(n):
    return [1 for x in range(n)]

def q_factoral(n):
    a  = [1]
    for i in range(n):
        a = poly_mult(a, q_number(i+1))
    return a

def poly_mult(a, b):
    length = len(a)+len(b)-1
    result = [0 for x in range(length)]
    for i in range(len(a)):
        # print(result)
        for k in range(len(b)):
            # print(i, k)
            result[i+k] += a[i] * b[k]
    return result

# https://en.wikipedia.org/wiki/Cyclic_sieving
def poly_div(a, b):
    result = []
    for i in range(len(a)-len(b)+1):
        result.append(a[i]//b[0])
        for j in range(len(b)):
            a[i+j] = a[i+j] - result[-1]*b[j]
    return result

def q_binomial_coef(n, k):
    return poly_div(poly_div(q_factoral(n), q_number(n-k)), q_number(k))


def q_catalan(n):
    return poly_div(poly_div(q_factoral(2*n), poly_mult(q_factoral(n), q_factoral(n))), q_number(n+1))
# def q_binomial_coef(n, k):

# print(q_number(3))

# for n in range(2, 10):
#     a = q_factoral(n)
#     print(a, sum(a))

# for n in range(1, 12):
#     print(q_catalan(n))
print(q_number(1))
for n in range(1, 7):
    for k in range(1, n):
        print(n, k)
        print(poly_div(q_factoral(n), q_number(n-k)))
# print(poly_div(q_factoral(4), [1, 2, 1]))
