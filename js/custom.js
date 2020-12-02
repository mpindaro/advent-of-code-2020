function getInput(funzione){
	document.getElementById('inputfile')
		.addEventListener('change', function() {

			var fr=new FileReader();
			fr.onload=function(){
				input=fr.result;
				funzione()
			}

			fr.readAsText(this.files[0]);
		})
}
