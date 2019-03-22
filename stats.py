import requests


def stats(name):
    try:
        data = requests.get("https://api.fortnitetracker.com/v1/profile/pc/" + name + "/",
                            headers={"TRN-Api-Key": "70961613-1369-445d-9d0c-77583457b40e"})
        work = data.json()
        pcstats = [work["lifeTimeStats"][8]["value"], work["lifeTimeStats"][9]["value"],
                   work["lifeTimeStats"][10]["value"],
                   work["lifeTimeStats"][11]["value"]]
    except:
        pcstats = [-1]
    try:
        data = requests.get("https://api.fortnitetracker.com/v1/profile/xbl/" + name + "/",
                            headers={"TRN-Api-Key": "70961613-1369-445d-9d0c-77583457b40e"})
        work = data.json()
        xboxstats = [work["lifeTimeStats"][8]["value"], work["lifeTimeStats"][9]["value"],
                     work["lifeTimeStats"][10]["value"],
                     work["lifeTimeStats"][11]["value"]]
    except:
        xboxstats = [-1]
    try:
        data = requests.get("https://api.fortnitetracker.com/v1/profile/psn/" + name + "/",
                            headers={"TRN-Api-Key": "70961613-1369-445d-9d0c-77583457b40e"})
        work = data.json()
        psnstats = [work["lifeTimeStats"][8]["value"], work["lifeTimeStats"][9]["value"],
                    work["lifeTimeStats"][10]["value"],
                    work["lifeTimeStats"][11]["value"]]
    except:
        psnstats = [-1]
    list = [int(pcstats[0]), int(xboxstats[0]), int(psnstats[0])]
    val = list.index(max(list))
    if max(list) == -1:
        return None
    if val == 0:
        return pcstats
    elif val == 1:
        return xboxstats
    else:
        return psnstats
