data = {}
def estimator(data):
	
	name = data['name']
	periodType = data['periodType']
	timeToElapse = data['timeToElapse']
	reportedCases = data['reportedCases']
	population = data['population']
	totalHospitalBeds = data['totalHospitalBeds']
	avgDailyIncomePopulation = data['avgDailyIncomePopulation']
	avgDailyIncomeInUSD = data['avgDailyIncomeInUSD']

# Cleaning Input Data
	periodType = periodType.lower()
	if periodType == 'days':
		timeToElapse = timeToElapse
	elif periodType == 'weeks':
		timeToElapse = timeToElapse*7
	else:
		timeToElapse = timeToElapse*30
	factor = timeToElapse // 3

# Computing Impact	
	currentlyInfected = reportedCases * 10
	infectionsByRequestedTime = currentlyInfected * 2**factor
	#Challenge 2
	severeCasesByRequestedTime = int(15 * 0.01 * infectionsByRequestedTime)
	currentlyAvailableBeds = totalHospitalBeds * 0.35
	hospitalBedsByRequestedTime = int(currentlyAvailableBeds - severeCasesByRequestedTime)

	#Challenge 3
	casesForICUByRequestedTime = int( 0.05 * infectionsByRequestedTime)
	casesForVentilatorsByRequestedTime = int(0.02 * infectionsByRequestedTime)
	dollarsInFlight = int((infectionsByRequestedTime 
						* avgDailyIncomePopulation 
						* avgDailyIncomeInUSD
						/ timeToElapse))

	# Computing SevereImpact
	SIcurrentlyInfected = reportedCases * 50
	SIinfectionsByRequestedTime = SIcurrentlyInfected * 2**factor
	#Challenge 2
	SIsevereCasesByRequestedTime = int(15 * 0.01 * SIinfectionsByRequestedTime)
	SIcurrentlyAvailableBeds = totalHospitalBeds * 0.35
	SIhospitalBedsByRequestedTime = int(SIcurrentlyAvailableBeds - SIsevereCasesByRequestedTime)

	#Challenge 3
	SIcasesForICUByRequestedTime = int( 0.05 * SIinfectionsByRequestedTime)
	SIcasesForVentilatorsByRequestedTime = int(0.02 * SIinfectionsByRequestedTime)
	SIdollarsInFlight = int((SIinfectionsByRequestedTime 
						* avgDailyIncomePopulation 
						* avgDailyIncomeInUSD
						/ timeToElapse))
	# Result
	global output
	output = {
			"data":{
		  "region":{
			"name":data["name"],
			"avgAge": data['avgAge'],
			"avgDailyIncomeInUSD": data['avgDailyIncomeInUSD'],
			"avgDailyIncomePopulation": data['avgDailyIncomePopulation']
		},
		"periodType":periodType,
		"timeToElapse":timeToElapse,
		"reportedCases":reportedCases,
		"population":population,
		"totalHospitalBeds":totalHospitalBeds
		},

		"estimate" : {
			"impact" : {
				"currentlyInfected" : currentlyInfected,
				"infectionsByRequestedTime" : infectionsByRequestedTime,
				"severeCasesByRequestedTime" : severeCasesByRequestedTime,
				"hospitalBedsByRequestedTime" : hospitalBedsByRequestedTime,
				"casesForICUByRequestedTime" : casesForICUByRequestedTime,
				"casesForVentilatorsByRequestedTime" : casesForVentilatorsByRequestedTime,
				"dollarsInFlight" : dollarsInFlight
				},
			"severeImpact" : {
				"currentlyInfected" : SIcurrentlyInfected,
				"infectionsByRequestedTime" : SIinfectionsByRequestedTime,
				"severeCasesByRequestedTime" : SIsevereCasesByRequestedTime,
				"hospitalBedsByRequestedTime" : SIhospitalBedsByRequestedTime,
				"casesForICUByRequestedTime" :SIcasesForICUByRequestedTime,
				"casesForVentilatorsByRequestedTime" : SIcasesForVentilatorsByRequestedTime,
				"dollarsInFlight" : SIdollarsInFlight
			}

		}

	}
	

	#estimate_schema = json.dumps(output, sort_keys =False, indent =4)
	#print(estimate_schema)
	return output
