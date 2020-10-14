# Containerized Selenium API

The main objective of this repository is to deploy a Docker container with
both, FastAPI and Selenium, to check the possibilities when we try to use
FastAPI to receive parameters, and run a selenium process in the background
to gather and parse data. This example uses the list of country populations,
available in Wikipedia and returns the data in a JSON format given the 
continent provided in the request.