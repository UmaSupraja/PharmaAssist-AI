// PharmaAssist AI - simple javascript

// ---------- chat window ----------
function openChat() {
  document.getElementById("chatBox").style.display = "block";
  document.getElementById("chatButton").style.display = "none";
}

function closeChat() {
  document.getElementById("chatBox").style.display = "none";
  document.getElementById("chatButton").style.display = "block";
}

// add a message to the chat
function addMessage(text, who) {
  var messages = document.getElementById("chatMessages");
  var p = document.createElement("p");
  p.className = who;
  p.innerText = text;
  messages.appendChild(p);
  messages.scrollTop = messages.scrollHeight;
}

// send the question to python and show the answer
function sendMessage() {
  var input = document.getElementById("chatInput");
  var question = input.value.trim();

  if (question == "") {
    return;
  }

  addMessage(question, "user");
  input.value = "";

  fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: question })
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      addMessage(data.response, "bot");
    })
    .catch(function () {
      addMessage("Sorry, cannot connect to the server.", "bot");
    });
}

// press Enter to send
document.getElementById("chatInput").onkeydown = function (event) {
  if (event.key == "Enter") {
    sendMessage();
  }
};


// ---------- store filter ----------
function filterStores(type) {
  var stores = document.getElementsByClassName("store");

  for (var i = 0; i < stores.length; i++) {
    if (type == "all" || stores[i].getAttribute("data-type") == type) {
      stores[i].style.display = "block";
    } else {
      stores[i].style.display = "none";
    }
  }
}


// ---------- prescription file check ----------
function checkFile() {
  var file = document.getElementById("fileInput").files[0];
  var message = document.getElementById("fileMessage");

  if (!file) {
    message.innerText = "Please choose a file first.";
    return;
  }

  var name = file.name.toLowerCase();
  var okType = name.endsWith(".jpg") || name.endsWith(".jpeg") ||
               name.endsWith(".png") || name.endsWith(".pdf");

  if (!okType) {
    message.innerText = "Only JPG, PNG or PDF files are allowed.";
  } else if (file.size > 10 * 1024 * 1024) {
    message.innerText = "File is bigger than 10 MB.";
  } else {
    message.innerText = "File OK: " + file.name + ". (Nothing was uploaded.)";
  }
}
