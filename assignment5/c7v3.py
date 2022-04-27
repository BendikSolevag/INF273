from operator import indexOf
from utils import *
from nbors import *
from methods import *
import time


def run_problem(problem, initial_solution):
    best_sol, best_sol_cost = alns(initial_solution, problem)
    return best_sol, best_sol_cost

problem = load_problem('./Call_7_Vehicle_3.txt')
print(problem["n_nodes"])
print(problem["VesselCargo"])
init_sol = [1, 1, 0, 0, 0, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]

init_cost = cost_function(init_sol, problem)

