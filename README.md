# DMC Collaborative K8S Interview Tasks

> The goal is to judge your familiarity with different technologies and see how you think about problems.

This is a very friendly audience. The goal is to work through the problems, helping everyone understand your thought process along the way. Googling, copy/paste, and asking questions is encouraged. More communication is better than less. Mostly, just have fun with it.


## Version Control

Checkout the interview repo from GitHub https://github.com/datamachines/99-problems

## Docker

The goal is to work through containerizing and running an application using Docker and Docker Compose

- Write a Dockerfile for a simple application contained in the `src/hello-world` folder of this repo.
  -- The service runs on port 5000
  -- It should extend the official `python:3` image
- Build the image from the dockerfile as `hello:dev`. 
  > Note that this may require using the host network as a build command parameter.
- Run the docker image and verify you can connect to it on port 5000 by curling `http://localhost:5000/Boss`.
- Stop and remove the container
- Retag and push the image to the local docker registry at `localhost:32000/python:3`
- Update a docker-compose file to run the image on the same port
  -- The service should expose port 5000
  -- It should run the hello:dev image
- Verify you can once again connect to it on port 5000 by curling `http://localhost:5000/Boss`.
- Stop the app

## Kubernetes

- List the nodes in the cluster
- Find out what storage is available in the cluster
- Create a new namespace `hello`
- Launch your hello-world app into the cluster using the kubernetes manifest in `dist/k8s/hello-world-deployment.yml`  
- What port is the app available on?
- Verify the deployment is visible from the local host by curling `http://localhost:<port>/Boss`
- Exec into the deployment pod and find the current username
- View the logs of the pod
- Delete the deployment and service.
