# Daytum 2-Day Spatial Data Analytics and Geostatistics Course 

This repository contains files related to a training class dated 05/07/2025.

Instructor: Michael Pyrcz, The University of Texas at Austin

#### Course Summary

Building from fundamental probability and statistics, we cover entire spatial data analytics and geostatistics best practice workflows from data preparation through to decision making. We will accomplish this with,

* Interactive lectures / discussion to cover the basic concepts

* Demonstrations of methods and workflows in Python 

* Hands-on experiential learning with well-documented workflows for accessibility


#### Course Objectives

Spatial data analytics and geostatistics for building spatial prediction and uncertainty models.

You will learn:

* spatial data debiasing

* quantification and modeling of spatial continuity / correlation

* spatial estimation with uncertainty

* spatial simulation for subsurface resource forecasting

* checking spatial models

* decision making with spatial uncertainty models

#### Course Schedule

Spatial Data Analytics and Geostatistics 2-day Short Course

| Day   | Time                  | Topic                                  | Objective                                                                                      |  Notes  | Demonstration | Interactivity |
|-------|-----------------------|----------------------------------------|------------------------------------------------------------------------------------------------|--------|---------|---------|
| Day 1 | 8:00 AM - 8:30 AM     | Course Overview                        | Walkthrough of the course plan, goals, methods and introductions                               | [Overview](/pdfs/CourseOverview.pdf) | | |
|       | 8:30 AM - 9:30 AM     | Introduction to Spatial Data Analytics and Geostatistics | Introduction to fundamental concepts and terminology, fit-for-purpose modeling and spatial modeling goals. | [Introduction](/pdfs/Introduction.pdf)    | | |
|       | 9:30 AM - 11:00 AM    | Probability                            | Both frequentist and Bayesian probability approaches.                                          | [Notes](/Pyrcz_UTCourse/02_Probability.pdf) | | [Dashboard](/notebooks/Interactive_Sivia_Coin_Toss.ipynb) |
|       | 11:00 AM - 12:00 PM   | Data Preparation                       | Introduction to data debiasing methods to correct for sampling bias. | [Notes](/Pyrcz_UTCourse/09b_Spatial_Debias.pdf) | [Demo](/notebooks/declustering.ipynb)| [Dashboard](/notebooks/Interactive_Declustering.ipynb) |
|       |   |                       | Introduction to bootstrap for uncertainty modeling. | [Notes](/Pyrcz_UTCourse/05_Univariate_Distributions.pdf) | [Demo](/notebooks/bootstrap.ipynb) | [Dashboard](/notebooks/Interactive_Bootstrap.ipynb) |
|       | 12:00 PM - 1:00 PM    | Lunch Break                            |                                                                                                |  | | |
|       | 1:00 PM - 2:00 PM     | Data Analytics                         | Univariate and multivariate statistical methods to support spatial modeling.                   | [Notes](/Pyrcz_UTCourse/08_Bivariate_Correlation.pdf) | [Demo](/notebooks/multivariate_analysis.ipynb) | [Dashbaord](https://github.com/daytum/geostats_training/blob/main/notebooks/Interactive_Correlation_Coefficient.ipynb) |
|       | 2:00 PM - 3:00 PM     | Spatial Continuity Calculation         | Introduce spatial continuity quantification by calculating variograms.                         | [Notes](/Pyrcz_UTCourse/10_Spatial_Calc.pdf) | [Demo](/notebooks/variogram_calculation.ipynb) | [Dashbaord](/notebooks/Interactive_Variogram_Calculation.ipynb) |
|       | 3:00 PM - 4:30 PM     | Spatial Continuity Modeling            | Introduce variogram modeling, omnidirectional, directional and nested structures.              | [Notes](/Pyrcz_UTCourse/11_Spatial_Interpretation_Modeling.pdf) | [Demo](/notebooks/variogram_modeling.ipynb) | [Dashboard](/notebooks/Interactive_Variogram_Calculation_Modeling.ipynb) |
| Day 2 | 8:00 AM - 10:00 AM    | Spatial Estimation                     | Introduce spatial estimators, theory and applications with kriging.                            | [Notes](/Pyrcz_UTCourse/12_Kriging.pdf)  | [Demo](/notebooks/kriging.ipynb) | [Dashboard](/notebooks/Interactive_Simple_Kriging.ipynb) |
|       | 10:00 AM - 12:00 PM   | Simulation and Uncertainty Modeling    | Cover the approaches to build a comprehensive uncertainty model, how to account for all salient sources of uncertainty? | [Notes](/Pyrcz_UTCourse/13_Simulation.pdf) | [Demo](/notebooks/simulation.ipynb) | [Dashbaord](/notebooks/Interactive_Simulation.ipynb) |
|       | 12:00 PM - 1:00 PM    | Lunch Break                            |                                                                                                |  | | |
|       | 1:00 PM - 2:00 PM     | Advanced Simulation                    | Cosimulation for bivariate simulation models. | [Notes](/Pyrcz_UTCourse/16_Cosimulation.pdf) | | |
|       |                       |                                        | Indicator simulation.                                                              | [Notes](/Pyrcz_UTCourse/14_Simulation_Indicator.pdf)  | [Demo](/notebooks/sisim.ipynb) | | 
|       |                       |                                        | Multiple point and object-based simulation.                                                    | [Notes](/Pyrcz_UTCourse/15_Simulation_Facies.pdf) | | |
|       | 2:00 PM - 3:00 PM     | Model Checking                         | Cover essential quality assurance methods for spatial, geostatistical models.                  | [Notes](/Pyrcz_UTCourse/16b_Model_Checking.pdf) | [Demo](/notebooks/model_checking.ipynb) | |
|       | 3:00 PM - 4:00 PM     | Decision Making with Uncertainty       | Present the workflow to make the best decision given an uncertainty model.                     | [Notes](/Pyrcz_UTCourse/16c_Decision_Making.pdf) |  | [Dashbaord](/notebooks/Interactive_Decision_Making.ipynb) |
|       | 4:00 PM - 4:30 PM     | Wrap-up, Review and Q&A                | Conclusion, group discussion and Plus/Delta exercise                                           |  |  | |

This is a nominal schedule. Note, we are learning and not schedule-driven; therefore the course delivery will adjust for the needs of the class. 

#### Beyond the Course

**There is Much More** – the building blocks can be reimplemented and expanded to address various other problems, opportunities. There is much more that we could cover,

* Additional Theory

* More Hands-on / Experiential

* Workflow Development

* Basics of Python / R

* Advanced Data Preparation

* Advanced Model QC

* Methods to Integrate More Geoscience and Engineering

* Integration of Machine Learning Spatial Modeling

We are happy to discuss other, advanced courses and custom courses to meet your teams' educational needs to add value at work with data science.

