$(function (){
var check = [];
function onFormSubmit(event){
	

	var data= $(event.target).serializeArray();

	var thesis = {};
	for (var i=0; i<data.length; i++){
		thesis[data[i].name] = data[i].value 

	}
	//send data to server
	var thesis_create_api = '/api/thesis';
	$.post(thesis_create_api,thesis,function(response){	 //url,data,callback
		if (response.status = "ok"){

		}});

	var list_element=$('<li id="item"' +'class="' + thesis.year + thesis.title + '">');
	list_element.html(thesis.year + ' ' + thesis.title + ' '  + ' <input type=button class="buttn btn-danger  btn-xs" value="Delete"  > ');
	

	if  ($('ul.thesis-list li').hasClass(thesis.year + thesis.title))
	{
		alert('Duplicate entries found! .Try Again');
	}
	else
	{
		$(".thesis-list").prepend(list_element) ;
		check.push(thesis.year + ' ' + thesis.title);

	}
	

	 return false;

}

function loadAllthesis_list() {
	var thesis_list_api = '/api/thesis';
	$.get(thesis_list_api, {}, function(response){
	console.log('thesis list', response)
	response.data.forEach(function(thesis){
	var full_name = thesis.year + ' ' + thesis.title;
	$('.thesis-list').append('<li>' + full_name +'</li>');
});
});
};


function DeleteEntry(event){
	$(this).parent().remove();
	$(this).closest('li').remove();
	
}
loadAllthesis_list()
$(document).on('click',  '.buttn' , DeleteEntry)
$('.create-form').submit(onFormSubmit)
$('.create-form').submit(function(onFormSubmit){ 
    this.reset();


});
});