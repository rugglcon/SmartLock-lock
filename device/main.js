var express = require('express');
var app = express();

function handle_res(res, err, data) {
  if(!err) {
    res.send(JSON.stringify({error: 0, data: data}));
  } else {
    res.send(JSON.stringify({error: err, data: data}));
  }
}

app.get('/open_lock', function(req, res) {
  var spawn = require('child_process').spawn;
  var proc = spawn('python', ['/home/pi/lock/main.py', 'open']);
});

app.get('/close_lock', function(req, res) {
	var spawn = require('child_process').spawn;
	var proc = spawn('python', ['/home/pi/lock/main.py', 'close']);
});

app.listen(8000, '0.0.0.0', function() {});
