import random
import math

def choose_random_elements_with_repetition(a, k):
    random_elements = random.choices(a, k=k)
    return random_elements

def german_tank_problem(elements):
    max_element = max(elements)
    num_distinct_elements = len(set(elements))    
    estimated_n =int(max_element*((num_distinct_elements)/(num_distinct_elements - 1)))
    return estimated_n

n=100
list_of_numbers = list(range(1, n+1))
k=13
sums=0
for i in range(1000):
    random_elements = choose_random_elements_with_repetition(list_of_numbers, k)
    sums+=german_tank_problem(random_elements)
print(sums/1000)

