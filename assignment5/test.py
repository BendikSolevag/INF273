from utils import cost_function, get_feasibility_cost, load_problem
from nbors import reorder_vehicle_calls
import numpy as np

n_nodes, n_vehicles, n_calls, Cargo, TravelTime, FirstTravelTime, VesselCapacity, LoadingTime, UnloadingTime, VesselCargo, TravelCost, FirstTravelCost, PortCost = load_problem('./Call_7_Vehicle_3.txt')


init_sol = np.array([4, 4, 7, 7, 4, 4, 0, 2, 2, 0, 1, 5, 5, 3, 3, 1, 0, 6, 6])
print(get_feasibility_cost(init_sol, n_vehicles, Cargo, TravelCost, FirstTravelCost, PortCost, TravelTime, FirstTravelTime, VesselCapacity, LoadingTime, UnloadingTime, VesselCargo))
print(cost_function(init_sol, n_vehicles, Cargo, TravelCost, FirstTravelCost, PortCost))
