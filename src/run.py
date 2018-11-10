from src.balancer import Balancer
import numpy as np
import random

balancer = Balancer()
accuracy = []
for n in range(10):
    transactions = [random.randrange(0, 10) for m in range(10)]
    print(balancer.total(np.array(transactions)), sum(transactions))
    accuracy.append(sum(transactions))
    print()
