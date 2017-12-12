# Governing Equations

## Introduction
The governing equations are basically a set of equations which model a physical phenomena. In our context, they will be a set of partial differential equations (PDEs), also called a system of PDEs. These equations define how different properties of interest vary within space and time. The properties of interest are called the dependent variables; and the space and time are called independent variables. The space is spanned by three mutually perpendicular axis denoted by the variables ![](https://latex.codecogs.com/gif.latex?x%2Cy%2Cz) and the variable for time is ![](https://latex.codecogs.com/gif.latex?t). Choosing an origin point in space-time and arbitrary values for variables ![](https://latex.codecogs.com/gif.latex?x%2Cy%2Cz) and ![](https://latex.codecogs.com/gif.latex?t), the complete three-dimensional space and time can be spanned. When we talk about solving the governing equations we need to restrict ourselves within a well-defined bounded region in space and time. This is called the solution-space. At the boundary of solution-space we have to define additional conditions to obtain unique solutions.

The dependent variables are properties like pressure, density, temperature, velocity etc. The distribution of these properties is the solution that we are interested in for, say, designing a product or understanding the physics. The system of PDEs is said to be closed when the number of dependent variables are equal to the number of equations. In many cases, the number of equations are lesser than the number of dependent variables. We have to then use models relating different properties, thus adding more equations, to close the system of governing equations. These models are mostly based on empirical relations or simplified assumptions.

## Generic form of system of PDEs
The governing PDEs used for simulation of various physical processes can be cast into a generic form,

![](https://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20W%7D%7B%5Cpartial%20t%7D&plus;%5Cfrac%7B%5Cpartial%20F_%7BC%7D%7D%7B%5Cpartial%20x%7D&plus;%5Cfrac%7B%5Cpartial%20G_%7BC%7D%7D%7B%5Cpartial%20y%7D&plus;%5Cfrac%7B%5Cpartial%20H_%7BC%7D%7D%7B%5Cpartial%20z%7D%3D%5Cfrac%7B%5Cpartial%20F_%7BD%7D%7D%7B%5Cpartial%20x%7D&plus;%5Cfrac%7B%5Cpartial%20G_%7BD%7D%7D%7B%5Cpartial%20y%7D&plus;%5Cfrac%7B%5Cpartial%20H_%7BD%7D%7D%7B%5Cpartial%20z%7D&plus;S%5C%20.)

Here, ![](https://latex.codecogs.com/gif.latex?W) is called the “conservative variable vector” or simply “conservative vector”. It is named so because the variables in this vector are an outcome of application of conservation laws. The vectors ![](https://latex.codecogs.com/gif.latex?F_%7BC%7D), ![](https://latex.codecogs.com/gif.latex?G_%7BC%7D) and ![](https://latex.codecogs.com/gif.latex?H_%7BC%7D) are called the “convective flux vectors”. They are named so because they contain the product of velocity with terms from conservative vector. Therefore capturing the phenomena of translation of conserved quantities due to convection currents. Most importantly, the convective flux vector does not contain any terms with space derivatives and is purely a function of the conservative vector. The vectors ![](https://latex.codecogs.com/gif.latex?F_%7BD%7D), ![](https://latex.codecogs.com/gif.latex?G_%7BD%7D) and ![](https://latex.codecogs.com/gif.latex?H_%7BD%7D) are called the “diffusion flux vectors”. All the terms with space derivatives are placed in these vectors. The diffusion flux vector is called so due to the fact that the spatial derivatives cause spreading (diffusion) or concentration of the quantities, even when the bulk fluid velocity is zero. The vector ![](https://latex.codecogs.com/gif.latex?S) is called the “source vector”. All the remaining terms in the governing equation, which can be integrated over finite control spatial volume, are clubbed together in this vector. Take a look at the example PDEs in section [sec:Few-common-PDEs](#few-common-governing-equations) to have a better understanding of these terms.

In many practical applications the solution at the steady state is sought, which implies that the time derivative term tends to zero. In such applications, solving time-accurate PDEs is unnecessary and probably inefficient. We may therefore, include an additional artificial-time derivative term which can be tweaked for efficient computations. The governing equations therefore becomes,

![](https://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20U%7D%7B%5Cpartial%5Ctau%7D&plus;%5Cfrac%7B%5Cpartial%20W%7D%7B%5Cpartial%20t%7D&plus;%5Cfrac%7B%5Cpartial%20F_%7BC%7D%7D%7B%5Cpartial%20x%7D&plus;%5Cfrac%7B%5Cpartial%20G_%7BC%7D%7D%7B%5Cpartial%20y%7D&plus;%5Cfrac%7B%5Cpartial%20H_%7BC%7D%7D%7B%5Cpartial%20z%7D%3D%5Cfrac%7B%5Cpartial%20F_%7BD%7D%7D%7B%5Cpartial%20x%7D&plus;%5Cfrac%7B%5Cpartial%20G_%7BD%7D%7D%7B%5Cpartial%20y%7D&plus;%5Cfrac%7B%5Cpartial%20H_%7BD%7D%7D%7B%5Cpartial%20z%7D&plus;S%5C%20.)

 Here, ![](https://latex.codecogs.com/gif.latex?%5Ctau) is called the artificial- or pseudo-time variable and ![](https://latex.codecogs.com/gif.latex?t) is the real-time variable. The vector ![](https://latex.codecogs.com/gif.latex?U) is called the artificial- or pseudo-conservative vector and to distinguish from this vector, ![](https://latex.codecogs.com/gif.latex?W) is now onwards called the real-conservative vector. The units of ![](https://latex.codecogs.com/gif.latex?U) and ![](https://latex.codecogs.com/gif.latex?W) are the same, however the actual terms may be completely different. It is a common practice to write ![](https://latex.codecogs.com/gif.latex?U%3DP%5C%2CW), where ![](https://latex.codecogs.com/gif.latex?P) is a pre-conditioner introduced to make the numerical calculations efficient and accurate. The flux and source vectors are functions of the artificial-conservative vector. For steady state simulations the term ![](https://latex.codecogs.com/gif.latex?%5Cpartial%20W/%5Cpartial%20t%3D0) and for unsteady simulations ![](https://latex.codecogs.com/gif.latex?%5Cpartial%20W/%5Cpartial%20t%5Cneq0). In both the cases (steady and unsteady simulations), the term ![](https://latex.codecogs.com/gif.latex?%5Cpartial%20U/%5Cpartial%5Ctau) must tend to zero for accepting the computational result.

There is another minor detail worth mentioning for the reason of completeness. The form in which the equations are written above is called the “conservative form”, not to be confused with the conservative vector. In this form, the space and time derivatives do not have any coefficients. The conservative form naturally arises when deriving the PDEs using conservation principles and applying the Gauss's theorem. This form is important for using the finite volume method, which will be explained in a later chapter.

The advantage of writing the governing equations in a generic form is that, now, it is possible to discuss the various CFD techniques in a well-defined setting. Also, this approach makes it possible to define computational models and write efficient computer programs which cater to a wide variety of applications which fit within this generic form.

## Different types of variables
When we say that we are solving the governing PDEs, it basically means that we are solving for the conservative vector in space and time with specified boundary and/or initial conditions. The variables in the conservative vector (called “conservative variables”) are generally not very intuitive to us humans. Instead, we like to deal with quantities that we can measure and have a feel for. For example, the quantity -- 'density ![](https://latex.codecogs.com/gif.latex?%5Ctimes) velocity' -- which is the conservative variable in the momentum equation is difficult to interpret as a whole, but we understand 'density' and 'velocity' separately. The so called “primitive variables” are simpler variables, introduced for this purpose. When we provide the inputs to the program or get outputs from the program, it is easier to deal with primitive variables.

The method of lines is a technique which is extensively used in the solution of time dependent PDEs. In this method it is useful to work with the so called “characteristics variables”. Even though in computer programs we do not very often use these variables, they form the basis of many CFD techniques. Also in some boundary conditions, such as non-reflective outlet boundary condition, the characteristics variables play an important role.

## Representation of governing equations in code
To solve the system of PDEs, we need to first come up with a way to represent the equations in code. The chosen way has to be generic and at the same time efficient and easy to integrate into the computational methods. As discussed above, different types of variables may be required at various places in the code and hence we need to convert between the different types. This is incorporated in the code through functions, 

![](https://latex.codecogs.com/gif.latex?U%5Cmapsto%20W%2C%5Cquad%20U%5Cmapsto%20V%2C%5Cquad%20V%5Cmapsto%20U%5Cquad%5Ctext%7Bwith%7D%5Cquad%20U%2CW%2CV%5Cin%5Cmathbb%7BR%7D%5E%7BN%7D%2C)

 where, ![](https://latex.codecogs.com/gif.latex?V) is the vector of primitive variables. ![](https://latex.codecogs.com/gif.latex?U) and ![](https://latex.codecogs.com/gif.latex?W) are the artificial- and real-conservative variables respectively, as described earlier, and ![](https://latex.codecogs.com/gif.latex?N) is the number of PDEs in the governing equations. In addition, the variables names will be needed for user interaction for input and output. The convective flux and the source vector can be described easily in terms of the artificial-conservative vector ![](https://latex.codecogs.com/gif.latex?U) and therefore we can define functions for them as, 

![](https://latex.codecogs.com/gif.latex?U%5Cmapsto%5Cleft%28F_%7BC%7D%2CG_%7BC%7D%2CH_%7BC%7D%5Cright%29%2C%5Cquad%20U%5Cmapsto%20S%5Cquad%5Ctext%7Bwith%7D%5Cquad%20U%2CF_%7BC%7D%2CG_%7BC%7D%2CH_%7BC%7D%2CS%5Cin%5Cmathbb%7BR%7D%5E%7BN%7D.)

The definition of functions for the diffusion flux vector requires not only the vector ![](https://latex.codecogs.com/gif.latex?U), but also spatial derivatives. Therefore, it is necessary to calculate the spatial variation of variables before calculation of the diffusive flux. The functions for calculation of the diffusive flux therefore are defined as,

![](https://latex.codecogs.com/gif.latex?%5Cleft%28U%2C%5Cnabla%20U%5Cright%29%5Cmapsto%5Cleft%28F_%7BD%7D%2CG_%7BD%7D%2CH_%7BD%7D%5Cright%29%5Cquad%5Ctext%7Bwith%7D%5Cquad%20U%2C%5Cnabla%20U%2CF_%7BD%7D%2CG_%7BD%7D%2CH_%7BD%7D%5Cin%5Cmathbb%7BR%7D%5E%7BN%7D.)

 Also, the characteristics of the convective flux and the material properties are necessary for the complete definition of the governing equations. There will also be some special cases when additional constitutive relations will be needed. All the above will be incorporated into the code by using an interface (abstract class). Hence making it extremely simple to adapt to any physical PDEs expressed in the generic form of the governing equations.
 
## Few common governing equations
Let us look at some of the governing equations that fit into the generic form. Many of these equations form the building blocks of research and are widely used in industry for design purposes. The derivation or detailed description of the governing physics is beyond the scope. For that it is recommended to refer to complete text on the specific subject. In the equations below, ![](https://latex.codecogs.com/gif.latex?%5Crho) is the mass density, ![](https://latex.codecogs.com/gif.latex?V%3D%5Cleft%28u%2Cv%2Cw%5Cright%29) is the velocity vector is a 3D Cartesian space, ![](https://latex.codecogs.com/gif.latex?p) is the absolute pressure, ![](https://latex.codecogs.com/gif.latex?E) is the total energy per unit mass (specific total energy), ![](https://latex.codecogs.com/gif.latex?T) is the temperature measured in Kelvin, ![](https://latex.codecogs.com/gif.latex?g%3D%5Cleft%28g_%7Bx%7D%2Cg_%7By%7D%2Cg_%7Bz%7D%5Cright%29) is the body force vector per unit mass, ![](https://latex.codecogs.com/gif.latex?%5Cdot%7Bq%7D) is the heat generation per unit volume, ![](https://latex.codecogs.com/gif.latex?%5Cmu) is the coefficient of dynamic viscosity, ![](https://latex.codecogs.com/gif.latex?k) is the coefficient of heat transfer due to conduction.

### Navier-Stokes equations
These equations are derived by applying the conservation principles of mass, momentum and energy to a fluid flow of single phase (gas or liquid). Furthermore, since the fluids are compressible, in general, the density is considered as a variable. The complete Navier-Stokes equations in three spatial dimensions comprises of 5 equations. They can be written in the generic form by substituting the following vectors,

![](https://latex.codecogs.com/gif.latex?%5Cbegin%7Barray%7D%7Bc%7D%20W%3D%5Cleft%5B%5Cbegin%7Barray%7D%7Bc%7D%20%5Crho%5C%5C%20%5Crho%20u%5C%5C%20%5Crho%20v%5C%5C%20%5Crho%20w%5C%5C%20%5Crho%20E%20%5Cend%7Barray%7D%5Cright%5D%2C%5Cquad%20F_%7BC%7D%3D%5Cleft%5B%5Cbegin%7Barray%7D%7Bc%7D%20%5Crho%20u%5C%5C%20%5Crho%20u%5E%7B2%7D&plus;p%5C%5C%20%5Crho%20uv%5C%5C%20%5Crho%20uw%5C%5C%20u%5Cleft%28%5Crho%20E&plus;p%5Cright%29%20%5Cend%7Barray%7D%5Cright%5D%2C%5Cquad%20G_%7BC%7D%3D%5Cleft%5B%5Cbegin%7Barray%7D%7Bc%7D%20%5Crho%20v%5C%5C%20%5Crho%20uv%5C%5C%20%5Crho%20v%5E%7B2%7D&plus;p%5C%5C%20%5Crho%20vw%5C%5C%20v%5Cleft%28%5Crho%20E&plus;p%5Cright%29%20%5Cend%7Barray%7D%5Cright%5D%2C%5Cquad%20H_%7BC%7D%3D%5Cleft%5B%5Cbegin%7Barray%7D%7Bc%7D%20%5Crho%20w%5C%5C%20%5Crho%20uw%5C%5C%20%5Crho%20vw%5C%5C%20%5Crho%20w%5E%7B2%7D&plus;p%5C%5C%20w%5Cleft%28%5Crho%20E&plus;p%5Cright%29%20%5Cend%7Barray%7D%5Cright%5D%2C%5C%5C%20%5C%5C%20F_%7BD%7D%3D%5Cleft%5B%5Cbegin%7Barray%7D%7Bc%7D%200%5C%5C%20%5Ctau_%7Bxx%7D%5C%5C%20%5Ctau_%7Byx%7D%5C%5C%20%5Ctau_%7Bzx%7D%5C%5C%20%5CTheta_%7Bx%7D%20%5Cend%7Barray%7D%5Cright%5D%2C%5Cquad%20G_%7BD%7D%3D%5Cleft%5B%5Cbegin%7Barray%7D%7Bc%7D%200%5C%5C%20%5Ctau_%7Bxy%7D%5C%5C%20%5Ctau_%7Byy%7D%5C%5C%20%5Ctau_%7Bzy%7D%5C%5C%20%5CTheta_%7By%7D%20%5Cend%7Barray%7D%5Cright%5D%2C%5Cquad%20H_%7BD%7D%3D%5Cleft%5B%5Cbegin%7Barray%7D%7Bc%7D%200%5C%5C%20%5Ctau_%7Bxz%7D%5C%5C%20%5Ctau_%7Byz%7D%5C%5C%20%5Ctau_%7Bzz%7D%5C%5C%20%5CTheta_%7Bz%7D%20%5Cend%7Barray%7D%5Cright%5D%2C%5Cquad%20S%3D%5Cleft%5B%5Cbegin%7Barray%7D%7Bc%7D%200%5C%5C%20%5Crho%20g_%7Bx%7D%5C%5C%20%5Crho%20g_%7By%7D%5C%5C%20%5Crho%20g_%7Bz%7D%5C%5C%20%5Crho%5Cleft%28g%5Ccdot%20V%5Cright%29&plus;%5Crho%5Cdot%7Bq%7D%20%5Cend%7Barray%7D%5Cright%5D.%20%5Cend%7Barray%7D)

 Some of the variables in these equations are already described before, the remaining are described here. The specific total energy, ![](https://latex.codecogs.com/gif.latex?E), consists of internal energy and kinetic energy, which can be written as,
 
 ![](https://latex.codecogs.com/gif.latex?E%3De&plus;%5Cfrac%7B%5Cleft%7CV%5Cright%7C%5E%7B2%7D%7D%7B2%7D%5C%20%2C)
 
 where, the internal energy, ![](https://latex.codecogs.com/gif.latex?e), is a function of flow properties like pressure and temperature, ![](https://latex.codecogs.com/gif.latex?e%3De%5Cleft%28p%2CT%5Cright%29), and ![](https://latex.codecogs.com/gif.latex?%5Cleft%7CV%5Cright%7C%3D%5Csqrt%7Bu%5E%7B2%7D&plus;v%5E%7B2%7D&plus;w%5E%7B2%7D%7D). The internal energy for gases can be written as ![](https://latex.codecogs.com/gif.latex?e%3Dc_%7Bv%7DT), based on the thermodynamic relation ![](https://latex.codecogs.com/gif.latex?de%3Dc_%7Bv%7DdT), assuming the specific heat capacity at constant volume, ![](https://latex.codecogs.com/gif.latex?c_%7Bv%7D), as a constant and the constant of integration as zero.

The viscous stress tensor can be written as ![](https://latex.codecogs.com/gif.latex?%5Ctau_%7Bij%7D) with ![](https://latex.codecogs.com/gif.latex?i%3Dx%2Cy%2Cz) and ![](https://latex.codecogs.com/gif.latex?j%3Dx%2Cy%2Cz). The first subscript denotes the direction of the viscous force and the second subscript denotes the face on which the stress is acting. The nine components of the tensor can be combined in a matrix as,

![](https://latex.codecogs.com/gif.latex?%5Ctau_%7Bij%7D%3D%5Cleft%5B%5Cbegin%7Barray%7D%7Bccc%7D%20%5Ctau_%7Bxx%7D%20%26%20%5Ctau_%7Bxy%7D%20%26%20%5Ctau_%7Bxz%7D%5C%5C%20%5Ctau_%7Byx%7D%20%26%20%5Ctau_%7Byy%7D%20%26%20%5Ctau_%7Byz%7D%5C%5C%20%5Ctau_%7Bzx%7D%20%26%20%5Ctau_%7Bzy%7D%20%26%20%5Ctau_%7Bzz%7D%20%5Cend%7Barray%7D%5Cright%5D%5C%20.)

In case of Newtonian fluids, these viscous stresses are assumed to be linearly proportional to gradients of velocity at the point. Thus providing with simplified relations for shear stresses as,

![](https://latex.codecogs.com/gif.latex?%5Ctau_%7Bij%7D%3D%5Cmu%5Cleft%28%5Cfrac%7B%5Cpartial%20u_%7Bi%7D%7D%7B%5Cpartial%20j%7D&plus;%5Cfrac%7B%5Cpartial%20u_%7Bj%7D%7D%7B%5Cpartial%20i%7D%5Cright%29&plus;%5Cdelta_%7Bij%7D%5Clambda%5Cnabla%5Ccdot%20V%5C%20.)

Here, ![](https://latex.codecogs.com/gif.latex?u_%7Bi%7D) denotes the velocity component, with ![](https://latex.codecogs.com/gif.latex?u_%7Bx%7D%3Du%2Cu_%7By%7D%3Dv%2Cu_%7Bz%7D%3Dw). The symbol ![](https://latex.codecogs.com/gif.latex?%5Cdelta_%7Bij%7D) is the Kronecker delta function which is defined as,
 
![](https://latex.codecogs.com/gif.latex?%5Cdelta_%7Bij%7D%3D%5Cbegin%7Bcases%7D%201%20%26%20i%3Dj%5C%5C%200%20%26%20i%5Cneq%20j%20%5Cend%7Bcases%7D%5C%20%2C)

the symbol ![](https://latex.codecogs.com/gif.latex?%5Clambda) is called the second coefficient of viscosity. Based on Stokes hypothesis, its value is generally taken as,

![](https://latex.codecogs.com/gif.latex?%5Clambda%3D-%5Cfrac%7B2%7D%7B3%7D%5Cmu)

and ![](https://latex.codecogs.com/gif.latex?%5Cnabla%5Ccdot%20V) is the divergence of the velocity field.

The energy diffusion terms come about due to the work done by the viscous stresses and the diffusion of energy due to conduction. They are related to the conservative vector with the following relations,

![](https://latex.codecogs.com/gif.latex?%5Cbegin%7Barray%7D%7Bc%7D%20%5CTheta_%7Bx%7D%3Du%5Ctau_%7Bxx%7D&plus;v%5Ctau_%7Bxy%7D&plus;w%5Ctau_%7Bxz%7D&plus;k%5Cfrac%7B%5Cpartial%20T%7D%7B%5Cpartial%20x%7D%5C%5C%20%5C%5C%20%5CTheta_%7By%7D%3Du%5Ctau_%7Byx%7D&plus;v%5Ctau_%7Byy%7D&plus;w%5Ctau_%7Byz%7D&plus;k%5Cfrac%7B%5Cpartial%20T%7D%7B%5Cpartial%20y%7D%5C%5C%20%5C%5C%20%5CTheta_%7Bz%7D%3Du%5Ctau_%7Bzx%7D&plus;v%5Ctau_%7Bzy%7D&plus;w%5Ctau_%7Bzz%7D&plus;k%5Cfrac%7B%5Cpartial%20T%7D%7B%5Cpartial%20z%7D%20%5Cend%7Barray%7D%5C%20.)

The diffusion coefficients like ![](https://latex.codecogs.com/gif.latex?%5Cmu) and ![](https://latex.codecogs.com/gif.latex?k)  are not constants over a wide range of flow quantities. The coefficient of viscosity, for example, for gases is highly influenced by the temperature. These coefficients can be calculated using lookup tables for flow variables, such as temperature, pressure etc. These lookups can be done very efficiently using search algorithms and linear interpolation. It is also common to use empirical relations, such as the Sutherland formula for coefficient of viscosity. For gases the Sutherland formula can be written as,

![](https://latex.codecogs.com/gif.latex?%5Cmu%3D%5Cmu_%7B0%7D%5Cfrac%7BT_%7B0%7D&plus;C%7D%7BT&plus;C%7D%5Cleft%28%5Cfrac%7BT%7D%7BT_%7B0%7D%7D%5Cright%29%5E%7B3/2%7D.)

This can be simplified to,
![](https://latex.codecogs.com/gif.latex?%5Cmu%3DC_%7B0%7D%5Cfrac%7BT%5E%7B3/2%7D%7D%7BT&plus;C%7D%5Cquad%5Ctext%7Bwith%7D%5Cquad%20C_%7B0%7D%3D%5Cmu_%7B0%7D%5Cfrac%7BT_%7B0%7D&plus;C%7D%7BT_%7B0%7D%5E%7B3/2%7D%7D%5C%20.)

The dynamic viscosity for air as function of temperature (in Kelvin) turns out to be,

![](https://latex.codecogs.com/gif.latex?%5Cmu%3D1.512%5Cfrac%7BT%5E%7B3/2%7D%7D%7BT&plus;120%7D%5Ctimes10%5E%7B-6%7D%5C%20%5Ctext%7BPa-s%7D.)

In cases of gases, the relation of Prandtl number is used for definition of ![](https://latex.codecogs.com/gif.latex?k) as,

![](https://latex.codecogs.com/gif.latex?k%3D%5Cfrac%7B%5Cmu%5C%2Cc_%7Bp%7D%7D%7BPr%7D%5C%20%2C)

and the Prandtl number, ![](https://latex.codecogs.com/gif.latex?Pr), is assumed to be constant. Similarly empirical relations can be used for calculation of the fluid coefficients as a function of local flow properties.

The source term in the momentum equations is a result of any body forces, such as gravity force, with force density vector per unit volume given by ![](https://latex.codecogs.com/gif.latex?g%3D%5Cleft%28g_%7Bx%7D%2Cg_%7By%7D%2Cg_%7Bz%7D%5Cright%29). The source term in the energy equation is a result of the work done by the body forces and heat generation with in the fluid due to sources, such as chemical reactions or radiation heat transfer.

Now, if we count the number of unknown variables, we can see that we have 6 unknowns -- ![](https://latex.codecogs.com/gif.latex?%5Crho%2Cu%2Cv%2Cw%2Cp%2CT) -- and only 5 equations. Therefore, we need another equation to close the system of equations. This is done by using the equation of state relating the pressure, density and temperature, ![](https://latex.codecogs.com/gif.latex?p%3Dp%5Cleft%28%5Crho%2CT%5Cright%29). For an ideal gas the equation of state is given as,

![](https://latex.codecogs.com/gif.latex?p%3D%5Crho%5Cfrac%7BR_%7Bu%7D%7D%7B%5Cdot%7Bm%7D%7DT%5C%20.)

 where, ![](https://latex.codecogs.com/gif.latex?R_%7Bu%7D%3D8.314%5Ctimes10%5E%7B3%7D%5Ctext%7B%20J/kmol-K%7D), is the universal gas constant and ![](https://latex.codecogs.com/gif.latex?%5Cdot%7Bm%7D) is the molar mass of the gas measured in kg/kmol (same as g/mol -- unit generally used in reference tables). In practice, the ratio ![](https://latex.codecogs.com/gif.latex?R_%7Bu%7D/%5Cdot%7Bm%7D) is replaced by a single gas constant ![](https://latex.codecogs.com/gif.latex?R). Thus, we get a simpler equation of state,
 
![](https://latex.codecogs.com/gif.latex?p%3D%5Crho%20RT%5C%20.)

In case of real gases at high temperatures or chemically reacting species, the equation of state will be more complicated. It is common to eliminate the specific heat capacity ![](https://latex.codecogs.com/gif.latex?c_%7Bv%7D) by introducing another constant ![](https://latex.codecogs.com/gif.latex?%5Cgamma), which is the ratio of specific heat capacity,

![](https://latex.codecogs.com/gif.latex?%5Cgamma%3D%5Cfrac%7Bc_%7Bp%7D%7D%7Bc_%7Bv%7D%7D%5C%20.)

Here, ![](https://latex.codecogs.com/gif.latex?c_%7Bp%7D) is the specific heat capacity at constant pressure. Using the thermodynamic relation, ![](https://latex.codecogs.com/gif.latex?R%3Dc_%7Bp%7D-c_%7Bv%7D), the constant ![](https://latex.codecogs.com/gif.latex?c_%7Bv%7D) can be written in terms of ![](https://latex.codecogs.com/gif.latex?%5Cgamma)  and ![](https://latex.codecogs.com/gif.latex?R) as,

![](https://latex.codecogs.com/gif.latex?c_%7Bv%7D%3D%5Cfrac%7BR%7D%7B%5Cgamma-1%7D%5C%20.)

The vector ![](https://latex.codecogs.com/gif.latex?U%3DPW), with ![](https://latex.codecogs.com/gif.latex?P) as a preconditioner matrix. The matrix ![](https://latex.codecogs.com/gif.latex?P) is chosen as an identity for high Mach flows, where the density changes are prominent. For low Mach flows (generally the case with liquid flows) there can be different ways of choosing a preconditioner. One of them is called the artificial compressibility method (given in another example later). More sophisticated methods, called the all-Mach number flow solvers, use a preconditioner as a function of the Mach number and therefore maintain the system well-conditioned in the complete domain and a wide range of Mach numbers.

TODO
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
