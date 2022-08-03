
var matriz = ["Baker","Businessman","Businesswoman","Carpenter",
			  "Cashier","Electrician","Farmer","Fisherman",
			  "Lifeguard","Mayor","Photographer",
			  "Ranger","Secretary","Waiter","Waitress"];

var contador = 0;

function numAleatorio(x) {
	return Math.floor(Math.random() * x);
}

var opcion = "error",numberAleatorio,contContinuar = 0,cont = 0;

 function guardarClick0() {
 	cleanOpciones(-1); /*limpia*/
 	opcion = document.getElementById('opcion0').value;
 	cleanOpciones(0);
 	modificarUndercover();
 }
 function guardarClick1() {
 	cleanOpciones(-1);
 	opcion = document.getElementById('opcion1').value;
 	cleanOpciones(1);
 	modificarUndercover();
 }
  function guardarClick2() {
  	cleanOpciones(-1);
 	opcion = document.getElementById('opcion2').value;
 	cleanOpciones(2);
 	modificarUndercover();
 }
  function guardarClick3() {
  	cleanOpciones(-1);
 	opcion = document.getElementById('opcion3').value;
 	cleanOpciones(3);
 	modificarUndercover();
 }

function modificarUndercover(){
	var pintarClick = document.getElementById('calificar');
	pintarClick.style.backgroundColor = "#78C800";
 	pintarClick.style.color = "white";
}

function cleanOpciones(x) {
	for(var i = 0; i < 4; i++){
		if (i == x) {
			document.getElementById('opcion' + i).style.backgroundColor = "#DDF4FF";
			document.getElementById('opcion' + i).style.borderColor = "#7ED2FA";
			document.getElementById('opcion' + i).style.color = "#1cb0f6";
			continue;
		}
		document.getElementById('opcion' + i).style.backgroundColor = "";
		document.getElementById('opcion' + i).style.borderColor = "";
		document.getElementById('opcion' + i).style.color = "";
	}
}

function opcionElegida() {
	if (document.getElementById('calificar').innerHTML != "Continuar") {
		document.getElementById('ocultarBoton').style.display = "none";
		document.getElementById('calificar').style.width = "";
			if (opcion == matriz[numberAleatorio]) {
				document.getElementById('sonidoCorrecto').play();
				document.getElementById('underNav').style.backgroundColor = "#B8F28B";
				document.getElementById('calificar').style.borderColor = "#78C800";
				document.getElementById('correcto').style.display = "flex";
				contador++;
			}
			else {
				document.getElementById('sonidoIncorrecto').play();
				document.getElementById('calificar').style.color = "white";
				document.getElementById('underNav').style.backgroundColor = "#FFC1C1";
				document.getElementById('calificar').style.backgroundColor = "#FF4B4B";
				document.getElementById('calificar').style.borderColor = "#FF4B4B";
				document.getElementById('falso').style.display = "flex";
				document.getElementById('completarFalso').innerHTML = "Solucion correcta:" + "<br>" + matriz[numberAleatorio];
			}
			document.getElementById('calificar').innerHTML = "Continuar";
	}
	contContinuar++;
	if (contContinuar == (matriz.length * 2)){
			document.getElementById('lineaDeProgreso2').style.width = "100%";
			alert("Juego finalizado\nCorrectos:" + contador + "/" + matriz.length);
			location.reload();	//Recarga la pagina
		}
	if (contContinuar % 2 == 0 && contContinuar != 0) {
		document.getElementById('correcto').style.display = "";
		document.getElementById('falso').style.display = "";
		document.getElementById('ocultarBoton').style.display = "";
		document.getElementById('calificar').innerHTML = "calificar";
		document.getElementById('calificar').style.backgroundColor = "";
		document.getElementById('calificar').style.color = "";
		document.getElementById('calificar').style.borderColor = "";
		document.getElementById('calificar').style.width = "";
		document.getElementById('underNav').style.backgroundColor = "";
		cleanOpciones(-1);
		opcion = "error";
		cont++;
		document.getElementById('lineaDeProgreso2').style.width = (( 100 / matriz.length ) * cont) + "%";
		funMain();
	}
}

function anadirValoresInputButton() {
	var posicionAleatorio = numAleatorio(4);
	for(var i = 0; i < 4; i++){
		document.getElementById("opcion" + i).value = matriz[numAleatorio(matriz.length)];
		if (posicionAleatorio == i) {
			document.getElementById("opcion" + i).value = matriz[numberAleatorio];			
		}
	}	
}
function funMain(){
	numberAleatorio = numAleatorio(matriz.length);
	var imagen = document.getElementById('contImagenes');
	imagen.style.background = "url(../static/imagen/" + matriz[numberAleatorio].toLowerCase() + ".png) no-repeat center top";
	imagen.style.backgroundSize = "contain";
	anadirValoresInputButton();
}

window.addEventListener('load',funMain());
