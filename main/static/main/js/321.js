('.faq_item_title_inner').on('click',function(){
        (this).parents('.faq_item').find('.faq_item_body').slideToggle(300);
        (this).toggleClass('open');
        if ((this).hasClass('show_all')){
                if ((this).hasClass('open')) {
                    (this).html('Свернуть все');
                ('.faq_item_title_inner:not(.open)').trigger('click');
            } else {
                (this).html('Смотреть все');
                ('.faq_item_title_inner.open').trigger('click');
            }
        }
    });