def is_prime(n):
    if n <= 1:
        return 0
    if n <= 3:
        return 1
    if  (n % 2 == 0 or n % 3 == 0):
        return 0
    i=5
    while (i * i <=n):
        if (n % i == 0 or n % (i+2) == 0):
            return 0
        i = i+6
    return 1

def count_prime(n):
    count =0
    prime_num = []
    for i in range(2,n+1):
        if (is_prime(i) == 1):
            prime_num.append(i)

    sum = prime_num[0]
    for i in range(1,len(prime_num)):
        sum += prime_num[i]
        if (sum > n):
            break
        if (is_prime(sum) == 1):
            count += 1

    return count

n = 100
print(count_prime(n))