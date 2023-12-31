# Generalized extrapolation methods based on compositions of a basic 2nd-order scheme
Coefficients for the article "Generalized extrapolation methods based on compositions of a basic 2nd-order scheme".

The file `loader.py` loads all coefficients into named variables and prints one of the sets of coefficents. Comments explain the corresponding integrators and figures in the paper. One may print the coefficients via editing the last code snippet at the end of `loader.py`

```python
print('Coefficents for Fig. 4, 5-stage integrator')
print(f'a1={a_ord8_91[:,0]}')
print(f'a2={a_ord8_91[:,1]}')
print(f'b={b_ord8_91}')
```
to print a different set of coefficients such as
```python
print('Coefficents for Fig. 1, k=2 integrator')
print(f'a={a_ord4_k2}')
print(f'b={b_ord4_k2}')
```
