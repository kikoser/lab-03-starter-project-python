from fastapi import APIRouter
import numpy as np

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}


@router.get("matrix")
def mult_matrices() -> dict:
    matrix1 = np.random.rand(10, 10)
    matrix2 = np.random.rand(10, 10)

    product = np.matmul(matrix1, matrix2)
    return {
        "matrix_a": matrix1.tolist(),
        "matrix_b": matrix2.tolist(),
        "product": product.tolist(),
    }
