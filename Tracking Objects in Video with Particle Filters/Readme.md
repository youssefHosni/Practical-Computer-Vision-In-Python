# Tracking Objects in Video with Particle Filters In Python

## Introduction 

Computer vision has made rapid progress in the last few years, thanks to improvements in training data and algorithms, as well as the availability of cheap GPUs and abundant labeled training datasets. One of the primary computer vision tasks is object tracking. Object tracking is used in the vast majority of applications such as video surveillance, car tracking, people detection, and tracking, etc. We will use a particle filter to track a moving object. Particle filters are powerful and efficient solutions to problems in robotics, artificial intelligence, and even finance.

![1_QV0wBEVUua2p3f1qnnylNw](https://user-images.githubusercontent.com/72076328/204287563-c7a54fd5-dfc6-4fcc-88b4-1b45f2eb7115.gif)

A particle filter is a generic algorithm for function optimization where the solution search space is searched using particles (sampling). So what does this mean? In our case, each particle incorporates tests on whether how it is likely that the object is at the position where the particle is. After the particles have been evaluated, the weights are assigned according to how good the particles are. Then the good particles are multiplied and the bad particles are removed through the re-sampling process.

The next particle generation then predicts where the object might be. Then this generation is evaluated, and the cycle repeats.

Opposed to the Kalman filter the particle filter can model non-linear object motion because the motion model should not be written as a state transition matrix like in the Discrete Kalman filter. Moreover, the particle filter is fairly easy to understand, but there is a negative thing: the performance of the filter depends on the particle number where the higher number of particles will lead to a better estimate, but it is more costly. Nevertheless, the particle filter is largely used for generic function optimization including object tracking. The figure below shows the two main steps of the particle filter: predict and correct.

![1_JNhxikwpmN1aMZOxFr7yUA](https://user-images.githubusercontent.com/72076328/204287766-43f94dde-0fe7-4722-8563-84c065246db5.png)

The cycle of a particle filter starts with the general probability densities. First, the filter predicts the next state from the provided state transition (e.g. motion model), then if applicable, the noisy measurement information is incorporated in the correction phase and the cycle is repeated after that.

## Methodology

* Loading & Displaying video frames using OpenCV
* Initializing a Particle Filter
* Moving Particles According to Their Velocity State
* Prevent Particles from Falling Off the Edges
* Measure Each Particle’s Quality
* Assign Weights to the Particles
* Resample Particles According to Their Weights
* Fuzz the Particles

## Final Output



