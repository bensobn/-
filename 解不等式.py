from sympy import symbols, solve, solve_univariate_inequality, S, FiniteSet
from sympy.core.relational import Relational
from sympy.sets.sets import Interval

def solve_inequality(inequality_input):
    # Define the symbol
    x = symbols('x')

    # Parse the inequality input
    inequality = eval(inequality_input)


    # Solve the inequality
    solution_set = solve_univariate_inequality(inequality, x, relational=False)

    # Convert the solution set to list format
    solution_list = []
    if isinstance(solution_set, Interval):
        solution_list.append(interval_to_list(solution_set.evalf()))
    elif isinstance(solution_set, FiniteSet):
        for point in solution_set:
            solution_list.append([round(point.evalf(),2)])
    else:
        for interval in solution_set.args:
            if isinstance(interval, Interval):
                solution_list.append(interval_to_list(interval.evalf()))
            elif isinstance(interval, FiniteSet):
                for point in interval:
                    solution_list.append([round(point.evalf(),2)])

    return solution_list

def interval_to_list(interval):
    # Convert an Interval to a list format
    lower = round(interval.start,2)
    upper = round(interval.end,2)

    # Replace infinity symbols with string representation
    lower = '-oo' if lower == S.NegativeInfinity else lower
    upper = 'oo' if upper == S.Infinity else upper

    return [lower, upper]

# Example usage:


# Solve x**2 - 4 >= 0
print(solve_inequality('10*(x**4-x**2)>=0'))