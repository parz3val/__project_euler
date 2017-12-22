''''
@author

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def prime_fact_max(number):
    for i in range(1,number):
        count = 2  # counter to test prime later
        # prime test.
        if (number % i == 0):  # Checks if the number is factorial.
            _num = int(number / i)
            for i in range(2, _num):
                if (_num % i == 0):
                    break
                else:
                    count = count + 1
        if (count == _num):
            return _num
            break




def main():
    num=600851475143
    print(prime_fact_max(num))






if __name__ == '__main__':
    main()
