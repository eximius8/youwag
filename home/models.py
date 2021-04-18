from django.db import models

from wagtail.core.models import Page, Orderable
from modelcluster.fields import ParentalKey
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.api import APIField

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    StreamFieldPanel,
    PageChooserPanel,
    ObjectList,
    TabbedInterface,
)


class HomePageCarouselImages(Orderable):
    """Between 1 and 5 images for the home page carousel."""

    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    caption = models.CharField(max_length=255, blank=True)

    panels = [
        ImageChooserPanel("carousel_image"),
        FieldPanel("caption"),

    ]

    api_fields = [
        APIField("carousel_image"),
    ]


class HomePage(Page):   


    parent_page_type = [
        'wagtailcore.Page'
    ]

    sub_header = models.CharField(max_length=200, null=True, blank=True)   



    api_fields = [
        APIField("sub_header"),        
        APIField("carousel_images"),
    ]

   
    content_panels = Page.content_panels + [
        FieldPanel("sub_header"),
        MultiFieldPanel(
            [InlinePanel("carousel_images", max_num=3, min_num=1, label="Image")],
            heading="Carousel Images",
        ),  
    ]

   

    class Meta:

        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"

    