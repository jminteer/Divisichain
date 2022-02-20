import math
import sys

def main(amount):
    input = 1 << amount
    inputcp = input

    # stored_fact = (-1,-1) #factorial, i

    # def next_fact_find(big):
    #     i = 0
    #     while(1):
    #         if(stored_fact[0] == -1 or stored_fact[0] > big):
    #             stored_fact
    #         if(math.factorial(i) > big):
    #             print("\rFound: " + str(i-1), end = "")
    #             return i-1
    #         i += 1


    i = 0
    while math.factorial(i) < input:
        i += 1

    i -= 1
    f = (math.factorial(i), i)

    def next_fact_find(big, f, i):
        while(1):
            if f[0] <= big:
                return i
            else:
                i -= 1
                f = (math.factorial(i), i)


    fact_array = []
    while(inputcp > 0):
        temp = next_fact_find(inputcp, f, i)
        fact_array += [temp]
        inputcp -= math.factorial(temp)
        print("\r" + str(temp), end = " ")

    ans = 0
    base_fact_array = [0] * (fact_array[0] + 1)
    for r in fact_array:
        ans += math.factorial(r)
        base_fact_array[r] += 1

    line = "++++++++++++++++++++++++++\n"
    print("\ndecimal input:  " + str(input))
    #print("\nfactorial array:  " + str(fact_array))
    print("\nbase factorial array:  " + str(base_fact_array))
    print("\n" + line + "Sizes bytes char")
    print("decimal: " + str(sys.getsizeof(input)) + " " + str(math.floor(math.log10(input))+1))
    char_count = 0
    for n in fact_array:
        char_count += math.floor(math.log10(n))+1
        char_count += 1
    print("factorial array: " + str(sys.getsizeof(fact_array)) + " " + str(char_count))
    char_count = 0
    for n in base_fact_array:
        if(n == 0):
            char_count += 1
            continue
        char_count += math.floor(math.log10(n))+1
        char_count += 1
    print("base factorial array: " + str(sys.getsizeof(base_fact_array)) + " " + str(char_count))
    print("\nMatching? " + str(ans == input))
    return base_fact_array