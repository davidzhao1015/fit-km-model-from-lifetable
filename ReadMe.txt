This project addresses a key need we encountered in the rare-disease epidemiology project: constructing a Kaplan–Meier curve and survival model using only a published life table.

To support this, I am converting the existing code into a reusable and well-documented Python notebook that explains each major step so that interested users can understand the workflow and reproduce the results. The modeling is implemented using the lifelines Python module.

I may extend the notebook further by estimating the mean time-to-event (or RMST) from the fitted Kaplan–Meier model.

In parallel, I plan to write a blog article that explains the *why* and *what* behind the notebook—highlighting the key assumptions required to reconstruct a Kaplan–Meier curve and model from life-table data.
