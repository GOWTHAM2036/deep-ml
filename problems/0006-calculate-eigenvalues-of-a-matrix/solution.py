import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	arr = np.array(matrix)
	values = np.linalg.eigvals(arr)
	eigenvalues = sorted(values, reverse=True)
	return eigenvalues