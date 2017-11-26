# Governing Equations

## Introduction

The governing equations are basically a set of equations which model a physical phenomena. In our context, they will be a set of partial differential equations (PDEs), also called system of PDEs. These equations define how different properties of interest vary within space and time. The properties of interest are called the dependent variables; and the space and time are called independent variables. The space is spanned by three mutually perpendicular axis denoted by the variables ![](https://latex.codecogs.com/gif.latex?x%2Cy%2Cz) and the variable for time is ![](https://latex.codecogs.com/gif.latex?t). Choosing an origin point in space-time and arbitrary values for variables ![](https://latex.codecogs.com/gif.latex?x%2Cy%2Cz) and ![](https://latex.codecogs.com/gif.latex?t), the complete three-dimensional space and time can be spanned. When we talk about solving the governing equations we need to restrict ourselves within a well-defined bounded region in space and time. This is called the solution-space. At the boundary of solution-space we have to define additional conditions to obtain unique solutions.

The dependent variables are properties like pressure, density, temperature, velocity etc. The distribution of these properties is the solution that we are interested in for, say, designing a product or understanding the physics. The system of PDEs is said to be closed when the number of dependent variables are equal to the number of equations. In many cases, the number of equations are lesser than the number of dependent variables. We have to then use models relating different properties, thus adding more equations, to close the system of governing equations. These models are mostly based on empirical relations or simplified assumptions.

## Generic form of system of PDEs
TODO
- temporal, convective, diffusive, source
- Advantages

## Different types of variables
TODO
- Conservative variables (artificial, real)
- Primitive variables
- Characteristic variables

## Representation of governing equations in code
TODO
- Variable conversions
- Convective flux
- Diffusive flux
- Source term

## Few common governing equations
TODO
- Navier-Stokes
- Euler
- Stokes
- shallow water
- Axi-symmetric flow
- 1D area-varying nozzle
- artificial compressibility
- Incompressible with and without heat transfer
- multiphase flow
- Turbulence
- Chemical reaction
- Road traffic
- Electromagnetism

## Important properties of physical PDEs
TODO
- Rotational invariance of system of PDEs
- Homogeneity of flux function
