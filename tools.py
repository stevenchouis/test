import math


def calculate_triangle_third_edge(edge_1, edge_2, is_third_edge_long_edge=True): 
    if is_third_edge_long_edge:
        return math.sqrt(edge_1*edge_1 + edge_2*edge_2)
    else:
        return math.sqrt(abs(edge_1*edge_1 - edge_2*edge_2))


def test():
    print("test")
