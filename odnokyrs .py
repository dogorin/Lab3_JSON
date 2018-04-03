
import json

data = {
 "Odnokyrs":
  [
 {
 "FIO": " Voskoboinikov S.V.",
 "address":
    {
 "Country": "Russia",
 "City": "Rostov-on-Don",
 "Street": "first Kracnodarskay"
    },
"contacs":
    {
 "VK": "https://vk.com/dogorin",
 "Twitter": "54ayha",
 "Primichanie": "lives alone",
    },
"phoneNumbers":
    [
 "812 123-1234",
 "916 123-4567"
    ]
 },
 {
 "FIO": "Alina Berejhay",
 "address":
    {
 "Country": "Russia",
 "City": "Rostov-on-Don",
 "Street": "Ddadad"
    },
"contacs":
    {
 "VK": "vk/i546121",
 "Twitter": "блааваб",
 "Primichanie": "Starosta",
    },
"phoneNumbers":
    [
 "812 123-1234",
 "916 123-4567"
    ]
 }
]
}
with open('result1.json','w') as outfile:
    json.dump(data,outfile)
