const express = require("express");
const { spawn } = require("child_process");
var cors = require("cors");
const app = express();
app.use(cors());

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.get("/name", (req, res) => {
  const process = spawn("python", ["recommend.py", req.query.name]);
  process.stdout.on("data", (data) => {
    console.log(data[0]);
    res.write(data.toString());
  });
  process.stderr.on("data", (data) => {
    console.log("outputerr", data.toString());
  });
  process.on("close", (code) => {
    res.end();
  });
});

app.listen(5000, () => {
  console.log("server started");
});
