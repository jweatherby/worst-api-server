# Worst API Server

For the Points developer take-home assignment, the following task is required. You are to build a tax calculator against this API. This server is pretty simple, only returning the tax rates for a given year. You are to calculate the amount of taxes owed by inputting a yearly salary, then displaying the different rates, the total amount owed and the effective tax rates.

## Instructions

* Download and run this server (see Getting Started)
* Build an application / tool in React or Python with the following criteria:
* * Fetches the tax rates from this API server
* * Take a yearly salary as input
* * Calculates and displays the total taxes owed for the salary
* * Displays the amount of taxes owed per band
* * Displays the effective rate

### Level 1

* Fetch the tax rates from this server at: http://localhost:5000/tax-brackets

### Level 2

* Fetch the tax rates by year: http://localhost:5000/tax-brackets/<2019|2020|...>

_Warning: this endpoint has gotchas_

### Level 3

* TBD


## Getting started

> docker pull jweatherby/worst-api-server
> docker run --init -p 5000:5000 -it jweatherby/worst-api-server

Navigate to http://localhost:5000. You should see a brief set of instructions.