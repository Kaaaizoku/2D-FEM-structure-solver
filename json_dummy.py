import json

dummyJSON = {
  "nodes": [
    {
      "id": 1,
      "x": 0,
      "y": 0.3
    },
    {
      "id": 2,
      "x": 0.3,
      "y": 0.3
    },
    {
      "id": 3,
      "x": 0.3,
      "y": 0
    }
  ],
  "members": [
    {
      "id": 1,
      "node1": 1,
      "node2": 2,
      "area": 0.1,
      "I": 0.01,
      "E": 200000
    },
    {
      "id": 2,
      "node1": 3,
      "node2": 2,
      "area": 0.1,
      "I": 0.01,
      "E": 200000
    }
  ],
  "boundaryConditions": [
    {
      "id": 1,
      "BC type": "fixed",
      "node": 1
    },
    {
      "id": 2,
      "BC type": "pinned",
      "node": 3
    }
  ],
  "pointLoads": [
    {
      "id": 1,
      "node": 2,
      "Fx": 1000,
      "Fy": 2500
    }
  ],
  "moments": [
    {
      "id": 1,
      "node": 1,
      "M": 0
    }
  ],
  "udls": [
    {
      "id": 1,
      "member": 1,
      "w": -100
    }
  ],
  "trussMemberIds": [
    2
  ],
  "frameMembers": [
    {
      "id": 1,
      "node1": 1,
      "node2": 2,
      "area": 0.1,
      "I": 0.01,
      "E": 200000
    }
  ],
  "trussNodes": [
    3,
    2
  ],
  "frameNodes": [
    {
      "id": 1,
      "x": 0,
      "y": 0.3
    }
  ]
}

dummyJSON = json.dumps(dummyJSON, indent=4)

print(type(dummyJSON))