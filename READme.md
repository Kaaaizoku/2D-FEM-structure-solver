# 2D Structural Solver

A free online tool for solving 2D structures is available at [2D Structural Solver](https://fefe-front.onrender.com/).

The solver can analyse trusses, frames, and combinations of both. Details of the implementation are available in the [Solver Implementation Notebook](Solver%20notebook.ipynb).

The solver has been tested on various structural configurations and loading conditions for verification.

---

# Cantilever Beam: Analytical vs FEM Results

## Problem

A 1 m cantilever beam is fixed at one end and subjected to an upward uniformly distributed load of \(100\ \text{N/m}\) and a counterclockwise end moment of \(100\ \text{N}\cdot\text{m}\).

- **Young's modulus:** \(E = 200{,}000\ \text{Pa}\)
- **Second moment of area:** \(I = 0.01\ \text{m}^4\)
- **Number of elements:** 5
- **Element length:** \(0.2\ \text{m}\)

![Cantilever beam displacement](images/displacement%20cl.png)

*Figure 1: Deflection of the cantilever beam under a UDL.*

![Cantilever beam reactions](images/reactions%20cl.png)

*Figure 2: Support reactions.*

![Cantilever beam bending moment](images/bending%20moment%20cl.png)

*Figure 3: Bending moment diagram.*

![Cantilever beam shear force](images/shear%20force%20cl.png)

*Figure 4: Shear force diagram.*

## Analytical and FEM Comparison

| Quantity | Analytical Result | FEM Result |
|---|---:|---:|
| Free-end displacement (m) | 0.031 | 0.031 |
| Bending moment at \(x = 0.4\ \text{m}\) (N·m) | -118 | -117.67 |
| Shear force at \(x = 0.4\ \text{m}\) (N) | 60 | Jumps from 50 to 70 |
| Reaction force (N) | -100 | -100 |
| Reaction moment (N·m) | -150 | -150 |

The solver uses cubic Hermite interpolation functions for the Euler–Bernoulli beam element. The displacement field is cubic; differentiating it twice gives a linear curvature and, consequently, a **linear bending-moment function within each element**. The corresponding shear force recovered by differentiating the bending moment is **constant within each element**.

Therefore, the FEM-recovered bending-moment and shear-force diagrams are piecewise linear and piecewise constant, respectively, and can differ from the analytical distributions under a UDL.

The calculated free-end displacement of \(0.03125\ \text{m}\) agrees with the FEM result of approximately \(0.031\ \text{m}\). The differences in the recovered bending-moment and shear-force diagrams can be reduced through mesh refinement.

---

# 2D Truss: Analytical vs FEM Results

## Problem Definition

A two-member planar truss has the following nodal coordinates:

- **Node 1:** \((0,0)\)
- **Node 2:** \((1,1)\)
- **Node 3:** \((2,0)\)

Both members have a length of \(L_e = \sqrt{2}\ \text{m}\). Nodes 1 and 3 are restrained in both translational directions. Loads are applied at node 2:

- **Horizontal load:** \(F_x = 20\ \text{N}\), acting to the right.
- **Vertical load:** \(F_y = 30\ \text{N}\), acting upward.

The material and cross-sectional properties are:

- **Young's modulus:** \(E = 200{,}000\ \text{Pa}\)
- **Cross-sectional area:** \(A = 0.1\ \text{m}^2\)

![Truss displacement](images/displacements%20tr.png)

*Figure 5: Truss deformation.*

![Truss reactions](images/reactions%20tr.png)

*Figure 6: Truss support reactions.*

## Analytical and FEM Comparison

### Analytical Results

The support reactions required for equilibrium are:

| Support | \(R_x\) (N) | \(R_y\) (N) |
|---|---:|---:|
| Node 1 | -25 | -25 |
| Node 3 | +5 | -5 |

The analytical displacements at node 2 are:

- **Horizontal displacement:** \(U_x = 0.0014142\ \text{m}\)
- **Vertical displacement:** \(U_y = 0.0021213\ \text{m}\)

These values are consistent with the FEM results when rounded to three decimal places: \(U_x \approx 0.001\ \text{m}\) and \(U_y \approx 0.002\ \text{m}\).

---

# Frame: ANSYS Comparison

## Problem Definition

A 2D portal frame consisting of three line members is analysed under a uniformly distributed load.

- **Geometry:** Horizontal span of \(0.6\ \text{m}\) and vertical height of \(0.5\ \text{m}\).
- **Cross-section:** I-section with area \(A = 3.8 \times 10^{-3}\ \text{m}^2\) and second moment of area about the \(y\)-axis, \(I_{yy} = 1.6817 \times 10^{-6}\ \text{m}^4\).
- **Material:** Young's modulus \(E = 200\ \text{GPa}\).
- **Boundary conditions:** Left end fixed and right end supported by a roller.
- **Loading:** Uniformly distributed load of \(10\ \text{N/mm}\), acting upward along the top horizontal member.

![ANSYS frame deformation](images/deformation%20fr.png)

*Figure 7: Frame results from ANSYS Mechanical.*

![Structural solver frame displacement](images/displacement%20fr.png)

*Figure 8: Frame results from the 2D Structural Solver.*

The results from the 2D Structural Solver agree with those from ANSYS Mechanical for the displacement of node 4 at the bottom-right corner.